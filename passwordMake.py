#!/usr/bin/env python

import os
from random import randrange

def randomName():
	"""find a random word from /usr/share/dict/words"""
	
	nameFile = open('/usr/share/dict/words','r')
	nameList = nameFile.readlines()
	nameFile.close()

	n = randrange(len(nameList))

	name = nameList[n-1].rstrip().capitalize()

	return name

def randomHex():
	"""find a random size random hex string"""
	n = randrange(4,16)
	return os.urandom(n).encode('hex')

def createPass():
	"""creates password"""
	name = randomName()
	number = randomHex()
	passwd = name + number
	return passwd

def main():
	for i in range(0,10):
		print createPass()

main()
