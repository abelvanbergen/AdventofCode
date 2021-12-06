lines = open("input.txt", "r").read().split('\n\n')
#lines = ['7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1', '22 13 17 11  0\n 8  2 23  4 24\n21  9 14 16  7\n 6 10  3 18  5\n 1 12 20 15 19', ' 3 15  0  2 22\n 9 18 13 17  5\n19  8  7 25 23\n20 11 10 24  4\n14 21 16 12  6', '14 21 17 24  4\n10 16 15  9 19\n18  8 23 26 20\n22 11 13  6  5\n 2  0 12  3  7']
input_nbrs = [int(x) for x in lines[0].split(',')]
boards = []
for line in lines[1:]:
	new=[]
	line = line.split('\n')
	for l in line:
		new.append([int(x) for x in l.split()])
	boards.append(new)

def	remove_nb_from_board(board, nb):
	for j in range(5):
		for i in range(5):
			if board[j][i] == nb:
				board[j][i] += 1000
	return (board)

def is_diagonal_bingo(board):
	total = 0
	for i in range(5):
		if board[i][i] >= 1000:
			total += 1
	if (total == 5):
		return (True)
	total = 0
	for x, y in [[4, 0], [3, 1], [2, 2], [1, 3], [0, 4]]:
		if board[x][y] >= 1000:
			total += 1
	if (total == 5):
		return (True)
	return (False)

def is_vertical_bingo(board):
	for i in range(5):
		total = 0
		for j in range(5):
			if board[j][i] >= 1000:
				total += 1
		if (total == 5):
			return (True)
	return (False)

def is_bingo(board):
	for i in range(5):
		if sum(board[i]) > 5000:
			return (True)
	# if is_diagonal_bingo(board):
	# 	return (True)
	if (is_vertical_bingo(board)):
		return (True)
	return (False)
		
def get_res_board(board, last_nb):
	total = 0
	# for line in board:
	# 	print(line)
	# quit()
	for j in range(5):
		for i in range(5):
			if board[j][i] < 1000:
				total += board[j][i]
	return (total * last_nb)

for nb in input_nbrs:
	for i, board in enumerate(boards):
		boards[i] = remove_nb_from_board(board, nb)
		if is_bingo(board):
			print(get_res_board(board, nb))
			quit()