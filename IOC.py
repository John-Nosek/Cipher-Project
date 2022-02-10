#John Nosek
#jnosek

import os
import sys
import matplotlib.pyplot as plt
from collections import Counter
import math
import collections

alph = "abcdefghijklmnopqrstuvwxyz"

def isLetter(char):
	return (char in alph)

def countLetters(text):
	count = 0
	for i in text:
		if(isLetter(i)):
			count += 1
	return count

def getIOC(text):
	letterCounts = []

	# Loop through each letter in the alphabet
	for i in range(len(alph)):
		count = 0
		for j in text:
			if j == alph[i]:
				count += 1
		letterCounts.append(count)
	# Loop through all letter counts
	total = 0
	for i in range(len(letterCounts)):
		ni = letterCounts[i]
		total += ni * (ni - 1)

	N = countLetters(text)
	c = 26.0 # Number of letters in the alphabet
	total = float(total) / ((N * (N - 1)))
	return total
abet = input("Please enter the alphabet of the file (-az or -b):")
filename = input("Enter the file to read the input from:")
infile = open(filename, 'r')
text = infile.read().lower()
text = text.replace(' ', '')

total = getIOC(text)
print("IOC: " + str(total))
print("Normalised IOC: " + str(total * 26.0))