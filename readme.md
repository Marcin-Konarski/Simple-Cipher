Simple Encryption and Decryption Program in Python

Author

This Python program was solely created by Marcin Konarski as a project for the "Kryptografia" subject in May 2024.

Disclaimer

This Python program is provided for educational and informational purposes only. Usage of this program is solely at the user's risk. I do not guarantee the accuracy, reliability, or suitability of this program for any particular purpose. By using this program, you agree that the developer shall not be liable for any direct, indirect, incidental, consequential, or punitive damages arising out of the use of or inability to use this program, even if advised of the possibility of such damages.

Licence

This program is open source and distributed under the MIT License. You are free to modify, distribute, and use this program for any purpose, subject to the terms and conditions of the license.

Description

This Python program provides functionality for encrypting and decrypting messages using a simple, custom encryption algorithm. Below is an extensive explanation of the program's components and functionalities.

Components

    1. Encryption Algorithm: The encryption algorithm involves several steps:
        Conversion of text into ASCII values: The message is converted into ASCII values and padded with zeros to adjust the size of the matrix.
        Key Generation: A hash key is created from the inputted key and resized to match the size of the matrix.
        Matrix Creation: The ASCII message and the key are converted into arrays of square matrices.
        Multiplication: The word matrix is multiplied with the key matrix for encryption.
        Further Encryption: The resulting values are further encrypted by dividing ASCII values by the length of a character list, shuffling the encrypted values, and joining them with the original index separated by a "~" symbol.

    2. Decryption Algorithm: The decryption algorithm involves reversing the steps of the encryption algorithm:
        Splitting: The encrypted message is split into letters and numbers.
        Sorting: The encrypted values are sorted based on their original index.
        Decryption: The sorted values are decrypted by creating matrices from the encrypted message and key, multiplying them, and converting the values into ASCII characters.

    3. Entropy Calculation and Time Measurement: The program calculates the entropy of the encrypted message to measure its randomness. Additionally, it measures the time taken to encrypt or decrypt a message.

    4. Simple Menu to Facilitate Easier Access to Its Functionalities

Usage

To use the program:

    Run the program and follow the menu instructions.
    Choose whether to encrypt or decrypt a message.
    Input the message and a secret key for encryption or the encrypted message and the decryption key for decryption. (Note that encryption key and decryption key are the same.)

Notes

    The program requires numpy library to be installed
    Ensure that the correct dependencies are installed before running the program.
    For encryption and decryption to work properly, ensure that the same key is used for both processes.
    The program uses ASCII encoding for text. Make sure the input text is compatible with ASCII encoding.

_______________________________________________________________________________________________________________________________________

Prosty program szyfrujący i deszyfrujący w Pythonie

Autor

Ten program w języku Python został stworzony wyłącznie przez Marcina Konarskiego jako projekt w ramach przedmiotu „Kryptografia” w maju 2024 roku.

Zastrzeżenie

Ten program jest udostępniany wyłącznie w celach edukacyjnych i informacyjnych. Korzystanie z tego programu odbywa się wyłącznie na ryzyko użytkownika. Nie gwarantuję dokładności, niezawodności ani przydatności tego programu do określonego celu. Korzystając z tego programu, użytkownik zgadza się, że deweloper nie ponosi odpowiedzialności za jakiekolwiek bezpośrednie, pośrednie, przypadkowe, wynikowe lub karne szkody wynikające z korzystania lub niemożności korzystania z tego programu, nawet jeśli został poinformowany o możliwości wystąpienia takich szkód.

Licencja

Ten program jest open source i jest rozpowszechniany na licencji MIT. Użytkownik może swobodnie modyfikować, rozpowszechniać i wykorzystywać ten program w dowolnym celu, z zastrzeżeniem warunków licencji.

Opis

Ten program jest napisany w języku Python i zapewnia funkcjonalność szyfrowania i odszyfrowywania wiadomości przy użyciu prostego, niestandardowego algorytmu szyfrowania. Poniżej znajduje się wyjaśnienie komponentów i funkcjonalności programu

Komponenty:

    1. Algorytm szyfrowania: Algorytm szyfrowania obejmuje kilka kroków:
        Konwersja tekstu na wartości ASCII: Wiadomość jest konwertowana na wartości ASCII i uzupełniana zerami w celu dostosowania rozmiaru macierzy.
        Generowanie klucza: Klucz hash jest tworzony na podstawie wprowadzonego klucza i dopasowywany do rozmiaru macierzy.
        Tworzenie macierzy: Wiadomość ASCII i klucz są konwertowane na tablice macierzy kwadratowych.
        Mnożenie: Macierz słów jest mnożona z macierzą klucza w celu zaszyfrowania.
        Dalsze szyfrowanie: Wynikowe wartości są dalej szyfrowane poprzez podzielenie wartości ASCII przez długość listy znaków, przetasowanie zaszyfrowanych wartości i połączenie ich z oryginalnym indeksem oddzielonym symbolem „~”.

    2. Algorytm deszyfrowania: Algorytm deszyfrowania polega na odwróceniu kroków algorytmu szyfrowania:
        Podział: Zaszyfrowana wiadomość jest dzielona na litery i cyfry.
        Sortowanie: Zaszyfrowane wartości są sortowane na podstawie ich oryginalnego indeksu.
        Deszyfrowanie: Posortowane wartości są odszyfrowywane poprzez utworzenie macierzy z zaszyfrowanej wiadomości i klucza, pomnożenie ich i przekształcenie wartości w znaki ASCII.

    3. Obliczanie entropii i pomiar czasu: Program oblicza entropię zaszyfrowanej wiadomości, aby zmierzyć jej losowość. Dodatkowo mierzy czas potrzebny do zaszyfrowania lub odszyfrowania wiadomości.

    4. Proste menu ułatwiające dostęp do jego funkcji

Użycie

Korzystanie z programu:

    Uruchomienie programu i postępowanie zgodnie z instrukcjami wyświetlanymi w menu.
    Wybranie, opcji: szyfrowanie, deszyfrowanie wiadomość lub wyjście.
    Wprowadzenie wiadomość i tajnego klucza do szyfrowania lub zaszyfrowaną wiadomość i klucz deszyfrujący do deszyfrowania. (Klucz służący do szyfrowania oraz ten do deszyfrowania są takie same.)

Uwagi

    Wymagane jest zainstalowanie biblioteki 'numpy'
    Przed uruchomieniem programu należy upewnić się, że zainstalowane zostały odpowiednie zależności.
    Aby szyfrowanie i deszyfrowanie działało poprawnie, należy upewnić się, że ten sam klucz jest używany w obu procesach.
    Program używa kodowania ASCII dla tekstu. Należy upewnić się, że tekst wejściowy jest zgodny z kodowaniem ASCII.