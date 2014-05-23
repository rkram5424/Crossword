import random as r

class Fillup2:
	board = [['#','#','#','#','#','#','#'],
	['#',' ',' ',' ',' ',' ','#'],
	['#',' ',' ',' ',' ',' ','#'],
	['#',' ',' ',' ',' ',' ','#'],
	['#',' ',' ',' ',' ',' ','#'],
	['#',' ',' ',' ',' ',' ','#'],
	['#','#','#','#','#','#','#']]

	wordBound5 = [8830,23874]
	f = open('wordlistSorted.txt','r')

	def __init__(self):
		pass

	def get_partials(self, x, y):
		end_arr = []
		spot = ' '
		count = 0
		while(spot != '#'):
			spot = self.board[x][y - count] #get top of room
			count += 1
		end_arr.append([x][y - count])

	def get_heads(self):
		for i in range (1,6): # 6 to be changed upon expansion
			for j in range (1,6): # 6 to be changed upon expansion
				if board[i][j-1] == '#' or board[i-1][j] == '#':
					if 

if __name__ == '__main__':
	Fillup2()