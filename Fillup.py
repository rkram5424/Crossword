import random as r

class Fillup:
	board = [[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ']]
	wordBound5 = [8830,23874]
	f = open('wordlistSorted.txt','r')

	def __init__(self):
		try:
			arr = [2,3,4];
			print(arr[3] == null)
		except IndexError:
			pass


		head_array = self.find_heads()
		self.fill_board()
		self.print_board()

	def find_bounds(self):
		# List must be sorted!
		# First by length.
		# Then alphabetically.
		f = open('wordlistSorted.txt','r')
		line = self.f.readlines()
		for i in range(1,len(lines)):



	def fill_board(self, head_array):
		line = self.f.readlines()
		for i in range(len(head_array)):
			match = False
			while match == False:
				if 
		place_word = line[r.randint(self.wordBound5[0], self.wordBound5[1])]
		self.addWord(0,0,'across',place_word)

	def find_heads(self):
		arr = []
		for i in range(5):
			for j in range(5):
				if i == 0 and j == 0:
					arr.append([[i,j],'across'])
					arr.append([[i,j],'down'])
				elif i == 0:
					arr.append([[i,j],'across'])
				else:
					arr.append([[i,j],'down'])
		return arr

	def addWord(self, x, y, dora, word):
		word = word.rstrip()
		if dora == 'down': # dora: down or across
			for i in range(len(word)):
				self.board[x + i][y] = word[i]
		else:
			for i in range(len(word)):
				self.board[x][y + i] = word[i]	

	def get_word(self, length, partial):
		word_length = len(partial)

	def match_words(self, partial, word):
		for i in range(len(word)):
			if partial[i] == '*':
				pass
			elif partial[i] != word[i]:
				return False
		return True

	def print_board(self):
		for i in range(5):
			for j in range(5):
				print self.board[i][j],
			print('')

if __name__ == '__main__':
	Fillup()