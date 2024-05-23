import string
import hashlib
import math
import random
import numpy as np
import re
from collections import Counter
import time
import sys

## simple generator to generate next letter, used to resize the key to the size of the message
def gen_next_letter(letters: str, char_index: int):
    yield letters[char_index]

## converts text into ascii values, and fills the remaining space with 0s
## to adjust the size of the matrix so it can be reshaped into a square matrix
def text_into_ascii(message: str, size_of_matrix: int) -> list[int]:
    ascii_values = list(map(ord, message))
    if (oversized_values := len(ascii_values) % size_of_matrix) != 0:
        ascii_values += [0] * (size_of_matrix - oversized_values)
    return ascii_values

## creates a hash key from the inputed key, and resizes it to the size of the matrix
def create_hash_key(key: str, length: int, size_of_matrix, decrypt=False) -> list[int]:
    key_hash = str(hashlib.sha256(key.encode()).hexdigest())
    key_hash = key_hash[:min(len(key_hash), size_of_matrix)]
    num_chars_to_fill = size_of_matrix - len(key_hash)
    for i in range(num_chars_to_fill):
        key_hash += next(gen_next_letter(key_hash, i % len(key_hash)))
    return list(map(ord, key_hash))

## creates an array of arrays that are the size of desired matrix from the ascii values array, and reshapes it into a array of square matrixes
def create_matrix(ascii_message: list[int], matrix_dimensions: tuple, size_of_matrix: int, is_key=False) -> list[np.ndarray]:
    if (oversized_values := len(ascii_message) % size_of_matrix) != 0:
        ascii_message += [0] * (size_of_matrix - oversized_values)
    sublists = [ascii_message[i:i + size_of_matrix] for i in range(0, len(ascii_message), size_of_matrix)]
    sublists_arrays = [np.array(sublist).reshape(*matrix_dimensions) for sublist in sublists]
    if is_key:
        return [np.array(element) for element in sublists_arrays if np.linalg.det(element.astype(np.float64)) != 0]
    return sublists_arrays

## multiplies the word matrix with the key matrix for encryption and word matrix with the inverse of the key matrix for decryption
def multiply(word: list[np.ndarray], key: list[np.ndarray], decrypt=False) -> list[int]:
    matrix = []
    for index, element in enumerate(word):
        if decrypt and (valid_range_of_key := key[index % len(key)]) is not None: ## That second condition is to avoid errors
            decrypted_matrix = np.dot(element.astype(np.int64), np.linalg.inv(valid_range_of_key).astype(np.float64))
            matrix.append(np.round(decrypted_matrix).astype(np.int64))
        elif not decrypt and (valid_range_of_key := key[index % len(key)]) is not None:
            matrix.append(np.dot(element.astype(np.int64), valid_range_of_key.astype(np.int64)))
        else:
            matrix.append(element.astype(np.int64))
    return [element for sublist in matrix for element in sublist.flatten() if element != 0]

## further encrypts the message by dividing ascii values by the length of the chars list
## and taking the quotient as numeric value and remainder as a character from the chars list
## then shuffles the encrypted values with their original index separated with "~"
def encrypt_shuffle(encrypted_list: list[int], chars: str) -> list[int]:
    encrypted_punctuations = []
    for element in encrypted_list:
        quotient, remainder = divmod(element, len(chars))
        encrypted_punctuations.append(str(chars[remainder]) + str(quotient))
    encrypted_with_index = [f"{element}~{index}" for index, element in enumerate(encrypted_punctuations)]
    shuffled = [encrypted_with_index[i] for i in np.random.permutation(len(encrypted_with_index))]
    return shuffled

## here is main enryption function, it creates matrixes from the word and key, multiplies them
## and creates that fancy pattern and shufles it. Each letter is separated with "|"
def encrypt_message(word: list[int], key: list[int], matrix_dimensions: tuple, size_of_matrix: int, chars: str) -> str:
    word_matrix = create_matrix(word, matrix_dimensions, size_of_matrix)
    key_matrix = create_matrix(key, matrix_dimensions, size_of_matrix, is_key=True)
    encrypted = multiply(word_matrix, key_matrix)
    shuffled_encrypted = encrypt_shuffle(encrypted, chars)
    return "|".join([str(element) for element in shuffled_encrypted])

## splits the encrypted message into letters and numbers
def split(strings: list[str]) -> list[tuple[str, int]]:
    result = []
    for s in strings:
        match = re.match(r'(\D+)(\d+)', s)
        if match:
            result.append((match.group(1), int(match.group(2))))
        else:
            result.append(('', s))
    return result

## splits each value representing original letter, then splits them into letters and their original indexes
## then sorts it by those indexes and covers those "letter index" values into still encrypted numerical values
def decrypt_sort(encrypted: str, size_of_matrix: int, chars: str) -> list[int]:
    if "|" in encrypted:
        encrypted_split = encrypted.split("|")
        encrypted_sorted = sorted(encrypted_split, key=lambda item: int(item.split("~")[1]) if "~" in item else 0)
        encrypted_sorted = [item.split("~")[0] for item in encrypted_sorted]
    else:
        encrypted_sorted = [ord(letter) for letter in encrypted]
    splitted = split(encrypted_sorted)
    result = []
    for element in splitted:
        result.append(int(chars.find(element[0]) + int(element[1]) * len(chars)))
    return result

## decrypts the message by creating matrixes from the encrypted message and key, multiplies them coverts the values into ascii characters,
## if unable to convert because wrong key was inserted, it chooses a random character from the chars list to avoid errors and show that the encryption was unsuccessful
def decrypt_message(encrypted: str, key: list[np.ndarray], matrix_dimensions: tuple, size_of_matrix: int, chars: str) -> str:
    decryption_sorted = decrypt_sort(encrypted, size_of_matrix, chars)
    decryption_matrix = create_matrix(decryption_sorted, matrix_dimensions, size_of_matrix)
    key_matrix = create_matrix(key, matrix_dimensions, size_of_matrix, is_key=True)
    decrypted = multiply(decryption_matrix, key_matrix, decrypt=True)
    try:
        decrypted_text = list(map(lambda x: chr(int(x)), decrypted))
    except:
        decrypted_text = list(random.choice(chars) for _ in decrypted)
    return "".join(decrypted_text)

def calculate_entropy(text):
    frequency_dict = Counter(text)
    probabilities = [float(frequency) / len(text) for frequency in frequency_dict.values()]
    return -sum([p * math.log2(p) for p in probabilities])

## calculates the entropy of the encrypted message and the time taken to encrypt/decrypt it
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        ed = func(*args, **kwargs)
        total = time.time() - start
        print(f"Time taken: {total}")
        print(f"Entropy: {calculate_entropy(ed)}")
        return ed
    return wrapper

## main encryption and decryption functions, they call the other functions and return the encrypted/decrypted message:
@timer
def encrypt(word, key, chars):
    size_of_matrix = (dimension := math.ceil(math.sqrt(len(word)))) ** 2
    matrix_dimensions = (dimension, dimension)
    word = text_into_ascii(word, size_of_matrix)
    key_hash = create_hash_key(key, len(word), size_of_matrix)
    return encrypt_message(word, key_hash, matrix_dimensions, size_of_matrix, chars)

@timer
def decrypt(to_decrypt, d_key, chars):
    if "~" not in to_decrypt and "|" not in to_decrypt:
        return "".join(list(random.choice(chars) for _ in to_decrypt))
    if not (length_of_word := math.ceil(to_decrypt.count("~"))):
        length = len(to_decrypt)
    else:
        length = length_of_word
    size_of_matrix = (dimension := math.ceil(math.sqrt(length))) ** 2
    matrix_dimensions = (dimension, dimension)
    d_key_hash = create_hash_key(d_key, length, size_of_matrix, decrypt=True)
    decrypted_text = decrypt_message(to_decrypt, d_key_hash, matrix_dimensions, size_of_matrix, chars)
    return decrypted_text

## main menu function, it calls the other functions and handles the user input
def menu():
    chars = ''.join(c for c in string.ascii_letters + string.punctuation if c not in ['~', '|', '\\'])
    while True:
        try:
            print("\033[34mMENU:\ne - Encrypt\033[0m")
            print("\033[34md - Decrypt\033[0m")
            print("\033[34mq - Exit\033[0m")
            choice = input("\033[32mEnter your choice: \033[0m")
            match choice.lower():
                case "e":
                    if not (word := input("\033[34mInput message: \033[0m")) or not (key := input("\033[34mInput a secret: \033[0m")):
                        print("\033[31mWrong Input!\033[0m")
                    else:
                        encrypted = encrypt(word, key, chars)
                        print("\033[32mEncrypted message: \033[0m", encrypted)
                case "d":
                    if not (d_word := input("\033[34mInput message to decrypt: \033[0m")) or not (d_key := input("\033[34mInput a secret: \033[0m")):
                        print("\033[31mInvalid Input\033[0m")
                    else:
                        decrypted_text = decrypt(d_word, d_key, chars)
                        print("\033[32mDecrypted Text: \033[0m", decrypted_text)
                case "q":
                    print("\033[31mExiting\033[0m")
                    sys.exit()  # Corrected line
                case _:
                    print("\033[31mInvalid input\033[0m")
        except Exception as e:
            print("Error occurred: ", e)
            print("\033[31mPress Enter to exit...\033[0m")


if __name__ == "__main__":
    menu()
