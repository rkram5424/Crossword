#!/usr/bin/env python
#
#  Crossword.py
#  
#  Copyright 2013 ryan <ryan@porta-penguin>
#  

# Imports and Globals, oh my!
import random as r
#import pygame
import urllib2

class Crossword:

	upperMax = 0
	sideMax = 0
	exes = 0
	f = open('wordlistSorted.txt','r')
	xBoard = [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
	[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
	[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
	[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
	[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
	[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
	[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
	[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
	[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
	[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
	[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
	[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
	[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
	[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
	[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']]
	
	#These are static now but I will have to make them dynamic if I change the wordlist
	wordBound3 = [0,2077]
	wordBound4 = [2077,8830]
	wordBound5 = [8830,23874]
	wordBound6 = [23874,52340]
	wordBound7 = [52340,92427]
	wordBound8 = [92427,141954]
	wordBound9 = [141954,193169]
	wordBound10 = [193169,237132]
	#wordBound11 = [,]
	#wordBound12 = [,]
	#wordBound13 = [,]
	#wordBound14 = [,]
	#wordBound15 = [,]

	def __init__(self):
		self.walls()
		self.center()
		self.fillBoard()
		#printBoard()
		self.writeHints()
		self.pgStuff()
		return 0

	def writeHints(self):
		acrossArray = []
		downArray = []
		numCount = 1
		for row in range(15):
			for column in range(15):
				if self.xBoard[row][column] == 'X':
					pass
				else:
					try:
						if (self.xBoard[row][column - 1] == 'X') or (self.xBoard[row - 1][column] == 'X') or(row == 0) or (column == 0):
							if (self.xBoard[row][column - 1] == 'X') or (column == 0):
								acrossArray.append(numCount)
							else:
								downArray.append(numCount)
							numCount = numCount + 1
						else:
							pass
					except: IndexError
		print ('ACROSS')
		for i in range(len(acrossArray)):
			print(acrossArray[i])
		print ('DOWN')
		for i in range(len(downArray)):
			print(downArray[i])

	def fillBoard(self):
		line = self.f.readlines()

		firstBlock = 0
		for i in range(15):
			if self.xBoard[0][i] == 'X':
				firstBlock = i
				break

		rootWord = ''
		if firstBlock == 3:
			rootWord = line[r.randint(self.wordBound3[0], self.wordBound3[1])]
		elif firstBlock == 4:
			rootWord = line[r.randint(self.wordBound4[0], self.wordBound4[1])]
		elif firstBlock == 5:
			rootWord = line[r.randint(self.wordBound5[0], self.wordBound5[1])]
		else:
			rootWord = line[r.randint(self.wordBound6[0], self.wordBound6[1])]
		self.addWord(0,0,'across', rootWord)

	def addWord(self, x, y, dora, word):
		word = word.rstrip()
		if dora == 'down':
			for i in range(len(word)):
				self.xBoard[x + i][y] = word[i]
		else:
			for i in range(len(word)):
				self.xBoard[x][y + i] = word[i]		

	def pgStuff(self):
		black    = (   0,   0,   0)
		white    = ( 255, 255, 255)
		green    = (   0, 255,   0)
		red      = ( 255,   0,   0)
		 
		# This sets the width and height of each grid location
		width  = 20
		height = 20
		 
		# This sets the margin between each cell
		margin = 1
		 
		# Create a 2 dimensional array. A two dimesional
		# array is simply a list of lists.
		grid = []
		for row in range(15):
		    # Add an empty array that will hold each cell
		    # in this row
		    grid.append([])
		    for column in range(15):
		        grid[row].append(0) # Append a cell
		 
		# Set row 1, cell 5 to one. (Remember rows and
		# column numbers start at zero.)
		 
		# Initialize pygame
		pygame.init()
		  
		# Set the height and width of the screen
		size = [315, 315]
		screen=pygame.display.set_mode(size)
		 
		# Set title of screen
		pygame.display.set_caption("Ryan's Crossword Generator")
		 
		#Loop until the user clicks the close button.
		done = False
		 
		# Used to manage how fast the screen updates
		clock = pygame.time.Clock()
		 
		# -------- Main Program Loop -----------
		while done == False:
			for event in pygame.event.get(): # User did something
				if event.type == pygame.QUIT: # If user clicked close
					done = True # Flag that we are done so we exit this loop
		 
		    # Set the screen background
			screen.fill(black)

			# Set up font 
			font1=pygame.font.SysFont('arial', 6)
			font2=pygame.font.SysFont('arial', 16, bold = True)

		    # Draw the grid
			for row in range(15):
				for column in range(15):
					color = white
					if self.xBoard[row][column] == 'X':
						color = black
					pygame.draw.rect(screen,color,[(margin+width)*column+margin,(margin+height)*row+margin,width,height])

			# Render numbers
			numCount = 1
			for row in range(15):
				for column in range(15):
					text=font1.render(str(numCount), True, (0, 0, 0))
					text2=font2.render(self.xBoard[row][column], True, (0, 0, 0))
					textpos = [(margin+width)*column+margin,(margin+height)*row+margin,width,height]#text.get_rect()
					textpos2 = [(margin+width)*column+margin + 5,(margin+height)*row+margin,width,height]#text.get_rect()
					if self.xBoard[row][column] == 'X':
						pass
					else:
						try:
							if (self.xBoard[row][column - 1] == 'X') or (self.xBoard[row - 1][column] == 'X') or(row == 0) or (column == 0):
								screen.blit(text, textpos)
								numCount = numCount + 1
							else:
								pass
						except: IndexError
						if not(self.xBoard[row][column] == '.'):
							screen.blit(text2, textpos2)
			
		    # Go ahead and update the screen with what we've drawn.
			clock.tick(20)
			pygame.display.flip()
		     
		# Be IDLE friendly. If you forget this line, the program will 'hang'
		# on exit.
		pygame.quit()

	# Builds the walls you see on the sides
	def walls(self):
		# plant seeds for walls
		upperWall1 = r.randint(4,6)
		upperWall2 = r.randint(upperWall1 + 4,11)
		sideWall1 = r.randint(4,6)
		sideWall2 = r.randint(sideWall1 + 4,11)
		
		# determine length for walls
		upperWall1Length = r.randint(2,4)
		upperWall2Length = r.randint(2,4)
		sideWall1Length = r.randint(2,4)
		sideWall2Length = r.randint(2,4)

		global upperMax
		global sideMax

		# define max wall lengths for use in center()
		if (upperWall1Length > upperWall2Length):
			upperMax = upperWall1Length
		else:
			upperMax = upperWall2Length

		if (sideWall1Length > sideWall2Length):
			sideMax = sideWall1Length
		else:
			sideMax = sideWall2Length

		# lengthen the walls
		self.buildWalls(upperWall1, 0, upperWall1Length)
		self.buildWalls(upperWall2, 0, upperWall2Length)
		self.buildWalls(sideWall1, 1, sideWall1Length)
		self.buildWalls(sideWall2, 1, sideWall2Length)

	#Lengthens the walls
	def buildWalls(self, wall, xy, length):
		if xy == 0: # if building upper wall
			for i in range(0, length):
				self.xBoard[wall][i] = 'X'
				self.mirrorPlace(wall, i)
		else: # if building side wall
			for i in range(0, length):
				self.xBoard[i][wall] = 'X'
				self.mirrorPlace(i, wall)

	# Builds the center of the board, which has a patter independent of the walls
	def center(self):
		for i in range(self.upperMax, 14 - self.upperMax):
			for j in range(self.sideMax,14 - self.sideMax):
				chance = r.randint(0,2) # gives each space a 33% chance
				if (chance == 1 and self.validPlace(i, j)):
					self.xBoard[i][j] = 'X'
					self.mirrorPlace(i, j)

	# Checks if [i][j] is a valid space before placing an X
	def validPlace(self, i, j):
		try:
			if ( # checks distant surroundings to prevent 2 letter spaces and lowers the amount of 3 letter spaces
				self.xBoard[i-2][j] == 'X' or self.xBoard[i+2][j] == 'X' or 
				self.xBoard[i-3][j] == 'X' or self.xBoard[i+3][j] == 'X' or 
				self.xBoard[i-4][j] == 'X' or self.xBoard[i+4][j] == 'X' or 
				self.xBoard[i][j-2] == 'X' or self.xBoard[i][j+2] == 'X' or 
				self.xBoard[i][j-3] == 'X' or self.xBoard[i][j+3] == 'X' or
				self.xBoard[i][j-4] == 'X' or self.xBoard[i][j+4] == 'X'
				):
				return False
			elif ( # ensures no X is 2 from the edge with space in between
			(i == 2 and self.xBoard[1][j] == ' ') or 
			(j == 2 and self.xBoard[i][1] == ' ') or 
			(i == 12 and self.xBoard[13][j] == ' ') or 
			(j == 12 and self.xBoard[i][13] == ' ')
				):
				return False
			else:
				return True
		except IndexError:
			pass

	# Makes sure the grid is radially symmetric
	def mirrorPlace(self, upperX, upperY):
		lowerX = 14 - upperX 
		lowerY = 14 - upperY 
		self.xBoard[lowerX][lowerY] = 'X'

	def countExes(self):
		global exes
		for i in range(0,15):
			for j in range(0,15):
				if self.xBoard[i][j] == 'X':
					exes += 1

	# Prints the board	
	def printBoard(self):
		for i in range(0,15):
			for j in range(0,15):
				if self.xBoard[i][j] == ' ':
					print ('.',) # Dots are easier to see :P
				else:
					print (xBoard[i][j],)
			print ('')
			
	def get_word(self, length, partial):
		word_length = len(partial)
		if word_length == 3:
			new_word = line[r.randint(self.wordBound3[0], self.wordBound3[1])]
		elif word_length == 4:
			new_word = line[r.randint(self.wordBound4[0], self.wordBound4[1])]
		elif word_length == 5:
			new_word = line[r.randint(self.wordBound5[0], self.wordBound5[1])]
		elif word_length == 6:
			new_word = line[r.randint(self.wordBound6[0], self.wordBound6[1])]
		elif word_length == 7:
			new_word = line[r.randint(self.wordBound7[0], self.wordBound7[1])]
		elif word_length == 8:
			new_word = line[r.randint(self.wordBound8[0], self.wordBound8[1])]
		elif word_length == 9:
			new_word = line[r.randint(self.wordBound9[0], self.wordBound9[1])]
		else:
			new_word = line[r.randint(self.wordBound10[0], self.wordBound10[1])]

if __name__ == '__main__':
	Crossword()

