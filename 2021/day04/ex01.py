lines = open("input.txt", "r").read().split('\n\n')
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

def is_bingo(line):
	for i in range(5):
		if (sum(line[i*5:i*5+5]>5000 or sum(line[i::5]>5000)
			return True
	return False


for nb in input_nbrs:
	for i, board in enumerate(boards):
		boards[i] = remove_nb_from_board(board, nb)
		if is_bingo(board):
			print(get_res_board(board, nb))
			quit()


for board in boards:

for i in range(len(boards)):

for i, board in enumerate(boards):