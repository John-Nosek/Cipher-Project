# Cipher-Project
A Caeser and Vigenère Cipher
#
The Caeser Cipher - A Caesar cipher is a simple method of encoding messages. Caesar ciphers use a substitution method where letters in the alphabet are shifted by some fixed number of spaces to yield an encoding alphabet. A Caesar cipher with a shift of 1 would encode an A as a B, an M as an N, and a Z as an A, and so on.
#
The Vigenère Cipher - The Vigenère cipher is similar to the Caeser method, but instead of using a single letter priming key, it uses a keyword and keys repeating itself.
#
The main program recieves a text file to either encrypt or decrypt using a Caeser or Vigenère Cipher. If any positive integer is inputted as the key, then that is the shift for the Caeser Cipher. If a '-1' is inputted, then the user is prompted for a text file that will be used as a key for a Vigenère Cipher.
#
The IOC program uses an inputed text file and calculates the Index of Coincidence. The Index of Coinicidence is a measure of how likely it is to draw two matching letters by randomly selecting two letters from a given text.
#
For example:
#
The file: Book2.txt is the file being encrypted.
#
The file: key.txt is used as the key for the Vigenère Cipher (the key is 'test').
#
The file: output.txt is the output after running the program.
