lines = open("input.txt", "r").read().split('\n\n')
input_nbrs = [int(x) for x in lines[0].split(',')]
boards = []
for line in lines[1:]:
	new=[]
	line = line.split('\n')
	for l in line:
		new.append([int(x) for x in l.split()])
	boards.append(new)
amount_of_boards = len(boards)

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
	if (is_vertical_bingo(board)):
		return (True)
	return (False)
		
def get_res_board(board, last_nb):
	total = 0
	print(last_nb)
	for j in range(5):
		for i in range(5):
			if board[j][i] < 1000:
				total += board[j][i]
	return (total * last_nb)

winners = []
winners_id = set()
for nb in input_nbrs:
	for i, board in enumerate(boards):
		boards[i] = remove_nb_from_board(board, nb)
		if i not in winners_id and is_bingo(board):
			winners_id.add(i)
			winners.append(board)
		if len(winners) == amount_of_boards:
			print(get_res_board(winners[-1], nb))
			return 