#!/usr/bin/env python

import os
from random import randrange

def randomWord():
	"""find a random word from /usr/share/dict/words"""
	
	wordFile = open('/usr/share/dict/words','r')
	wordList = wordFile.readlines()
	wordFile.close()

	n = randrange(len(wordList))

	word = wordList[n-1].rstrip().capitalize()

	return word

def randomHex():
	"""find a random size random hex string"""
	n = randrange(4,16)
	return os.urandom(n).encode('hex')

def createPass():
	"""creates password"""
	word = randomWord()
	number = randomHex()
	passwd = word + number
	return passwd

def main():
	for i in range(0,10):
		print createPass()

main()
