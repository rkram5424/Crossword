#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Crossword.py
#  
#  Copyright 2013 ryan <ryan@porta-penguin>
# 

import urllib, urllib2, webbrowser, re


def main():
	pass

def getWords():
	f = open('words.txt', 'w')

def getMovies():
	f = open('movies.txt', 'w')
	rootUrl = 'http://http://en.wikipedia.org/wiki/List_of_films:_'
	letters = ['numbers','A','B','C','D','E','F','G','H','I','J-K','L','M','N-O','P','Q-R','S','T','U-V-W','X-Y-Z']
	for i in range(letters.length):
		response = urllib2.urlopen(rootUrl + letters[i])
		pageSource = response.read()

def getBooks():
	f = open('books.txt', 'w')

def getShows():
	f = open('shows.txt', 'w')

def combineLists():
	pass

def stringify(name):
	name = name.replace('10','ten')
	name = name.replace('11','eleven')
	name = name.replace('12','twelve')
	name = name.replace('13','thirteen')
	name = name.replace('14','fourteen')
	name = name.replace('15','fifteen')
	name = name.replace('16','sixteen')
	name = name.replace('17','seventeen')
	name = name.replace('18','eighteen')
	name = name.replace('19','nineteen')
	name = name.replace('20','twenty')
	name = name.replace('21','twenty one')
	name = name.replace('1','one')
	name = name.replace('2','two')
	name = name.replace('3','three')
	name = name.replace('4','four')
	name = name.replace('5','five')
	name = name.replace('6','six')
	name = name.replace('7','seven')
	name = name.replace('8','eight')
	name = name.replace('9','nine')
	name = name.replace('&','and')
	name = name.replace('\'','')
	name = name.replace('*','')
	name = name.replace('_','')
	name = name.replace('?','')
	name = name.replace('!','')
	name = name.replace('.','')
	name = name.replace(' ','')
	return name

if __name__ == '__main__':
	main()