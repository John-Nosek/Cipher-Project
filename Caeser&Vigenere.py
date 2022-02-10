#John Nosek
#jnosek

import os
import sys
import matplotlib.pyplot as plt
from collections import Counter
import math

def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)):
        yield chr(c)
    yield chr(ord(c2))

azalphabet = [a for a in char_range('A', 'Z')]

binalphabet = [a for a in char_range('\0', '\xff')]

def orderedCount(text, alphabet):
    count = Counter(text)
    ordered = [0] * len(alphabet)
    for index, a in enumerate(alphabet):
        ordered[index] = count[a]
    return ordered

def readazfile(filename):
    """Reads a text file and returns an array of only letters A-Z upcased"""
    f = open(filename, "r", encoding="utf-8")
    text = f.read()
    s = set(azalphabet)
    return [c.upper() for c in text if c.upper() in s]
    print(c.upper() for c in text if c.upper() in s)


def readbinaryfile(filename):
    """returns the file as an array of single character strings"""
    return [chr(b) for b in open(filename, "rb").read(-1)]
    print(chr(b) for b in open(filename, "rb").read(-1))

def envigenere(key, txt):
    k = len(key)
    counter = 0
    cipher = ""

    for c in txt:
        if c.isalpha() == False:
            cipher += c

        else:
            new_c = ord(c) + (ord(key[counter % k]) % 32 - 1)

            if ((c.isupper()) and new_c > 90) or new_c > 122:
                new_c = new_c - 26

            cipher += chr(new_c)

            counter += 1

    return cipher

def devigenere(key, txt):
    k = len(key)
    counter = 0
    cipher = ""

    for c in txt:
        if c.isalpha() == False:
            cipher += c

        else:
            new_c = ord(c) - (ord(key[counter % k]) % 32 - 1)

            if ((c.islower()) and new_c < 65) or new_c < 97:
                new_c = new_c + 26

            cipher += chr(new_c)

            counter += 1

    return cipher

def encrypt(text, key):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char == ' ':
            result += ' '
        elif char.isupper():
            result += chr((ord(char) + key - 65) % 26 + 65)
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)
    return result


def decrypt(text, key):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char == ' ':
            result += ' '
        elif char.isupper():
            result += chr((ord(char) - key - 65) % 26 + 65)
        else:
            result += chr((ord(char) - key - 97) % 26 + 97)
    return result

type = input("Please indicate if you are encrypting or decrypting (enc/dec):")

abet = input("Please enter the alphabet of the file (-az or -b):")

filename = input("Enter the file to read the input from:")
if abet == '-az':
    infile = open(filename, 'r')
    text = infile.read()
if abet == '-b':
    readbinaryfile(filename)
    print(readbinaryfile(filename))

outfilename = input("Enter the file to write the output to:")
outfile = open(outfilename, "w")

if abet == '-az':
    readazfile(filename)
if abet == '-b':
    readbinaryfile(filename)

length = int(input("Please enter the type of key (-1 to use a word or a positive integer for a consistent shift):"))

if length == -1:
    if type == 'enc':
        keyfile = input("Please enter the file for the key you would like to use:")
        infile = open(keyfile, 'r')
        keyfile = infile.read()
        ex = open(outfilename, "w")
        ex.write(envigenere(keyfile, text))
    if type == 'dec':
        keyfile = input("Please enter the file for the key you would like to use:")
        infile = open(keyfile, 'r')
        keyfile = infile.read()
        ex = open(outfilename, "w")
        ex.write(devigenere(keyfile, text))


if length != -1:
    if type == 'enc':
        key = length
        ex = open(outfilename, "w")
        ex.write(encrypt(text, key))
    if type == 'dec':
        key = length
        ex = open(outfilename, "w")
        ex.write(decrypt(text, key))



