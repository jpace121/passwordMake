#!/usr/bin/env python

import os
from random import randrange
import pickle

"""
TODO:
	Make more API-ish
"""

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

def makePass():
	"""make password and write it to password file"""
	site = raw_input("Enter Site password is for: ")
	description = raw_input("Enter short description of site: ")
	passwd = createPass()

	passTuple = site, description, passwd

	passFile = open('./passFile.pckl','r+')
	passArray = pickle.load(passFile)
	passFile.close()

	passArray.append(passTuple)

	passFile = open('./passFile.pckl','w')
	pickle.dump(passArray,passFile)
	passFile.close()

def getPass():
	"""Gets Password from file"""
	passFile = open('./passFile.pckl','r')
	passArray = pickle.load(passFile)
	passFile.close()

	wantedSite = raw_input("What Site do you want the password for: ")

	for passTuple in passArray:
		print passTuple
		if passTuple[0] == wantedSite:
			passwd = passTuple[2]
			break
		else:
			passwd = "Not Found!"
	
	print passwd

def setup():
	"""setup initial passsArray"""
	passArray = []
	passFile = open('./passFile.pckl','w')
	pickle.dump(passArray,passFile)
	passFile.close()

#def main():
#	makePass()

#main()
