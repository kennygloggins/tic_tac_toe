import sys
import locale
from numpy import inf



global board
players = ['X', 'O']
board = [[' ' for k in range(3)] for i in range(3)]
board[1][1] = 'X'
scores = {'X': 1, 'O': -1, 'tie': 0}
square = {1: (0, 0), 2:  (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1),
		6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2)}


def Display(again):
	if again == 0:
		print(f'''
		+-----+-----+-----+
		|     |     |     |
		|  1  |  2  |  3  |
		|     |     |     |
		+-----+-----+-----+
		|     |     |     |
		|  4  |  5  |  6  |
		|     |     |     |
		+-----+-----+-----+
		|     |     |     |
		|  7  |  8  |  9  |
		|     |     |     |
		+-----+-----+-----+
		''')
	if again == 1 or again == 0:
		print(f'''
		+-----+-----+-----+
		|     |     |     |
		|  {board[0][0]}  |  {board[0][1]}  |  {board[0][2]}  |
		|     |     |     |
		+-----+-----+-----+
		|     |     |     |
		|  {board[1][0]}  |  {board[1][1]}  |  {board[1][2]}  |
		|     |     |     |
		+-----+-----+-----+
		|     |     |     |
		|  {board[2][0]}  |  {board[2][1]}  |  {board[2][2]}  |
		|     |     |     |
		+-----+-----+-----+
		''')
	else:
		pass


def EnterMove(again=0):
	Display(again)
	player_move = input("Please pick a box to play by it's corresponding number:")
	k, i = square[int(player_move)]
	if board[k][i] != ' ':
		print("Invalid choice, please try again.")
		EnterMove(2)
	board[k][i] = 'O'
	Display(1)
	result = VictoryFor()
	if result == None:
		ai()
	else:
		Winner(result)


def VictoryFor():
	empty = False
	for lst in board:
		if lst.count(' '):
			empty = True
	if empty:
		for player in players:
			for i in range(3):
				result = []
				for k in board:
					if k[i] == player: 
						result.append(k[i])
						if len(result) == 3: return player
		for player in players:
			for i in range(3):
				if board[i][i] == player:
					result = []
					result.append(player)
					if len(result) == 3: return player
				if board[-i][i] == player:
					result = []
					result.append(player)
					if len(result) == 3: return player
		for player in players:
			result = [i for i in range(3) if board[i][i] == player]
			if len(result) == 3: return player
			result = [i for i in range(3) if board[i][-(i+1)] == player]
			if len(result) == 3: return player
		return None
	else:
		return 'tie'


def minimax(board, depth, isMiniMax):
	result = VictoryFor()
	if result != None:
		score = scores[result]
		return score

	if isMiniMax:
		bestScore = float(-inf)
		for k in range(len(board)):
			for i in range(len(board[k])):
				if board[k][i] == ' ':
					board[k][i] = 'X'
					score = minimax(board, depth+1, False)
					board[k][i] = ' '
					bestScore = max(score, bestScore)
		return bestScore
	else:
		bestScore = float(inf)
		for k in range(len(board)):
			for i in range(len(board[k])):
				if board[k][i] == ' ':
					board[k][i] = 'O'
					score = minimax(board, depth+1, True)
					board[k][i] = ' '
					bestScore = min(score, bestScore)
		return bestScore

def ai():
	bestScore = float(-inf)
	for k in range(len(board)):
		for i in range(len(board[k])):
			if board[k][i] == ' ':
				board[k][i] = 'X'
				score = minimax(board, 0, False)
				board[k][i] = ' '
				if score > bestScore:
					bestScore = score
					best, Move = k, i
	board[best][Move] = 'X'
	result = VictoryFor()
	if result == None:
		EnterMove(1)
	else:
		Winner(result)



def Winner(player):
	if player == 'O':
		again = input('Congradualtions You Won! Play again?')
	elif player == 'tie':
		Display(1)
		again = input('You tied! play again?')
	else:
		Display(1)
		again = input('You lost! Play again?')
	if again.lower() == 'yes' or again.lower() == 'y':
		for k in range(len(board)):
			for i in range(len(board[k])):
				board[k][i] = ' '
		board[1][1] = 'X'
		EnterMove()
	else:
		exit()

EnterMove()
