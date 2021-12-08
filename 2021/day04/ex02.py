def is_bingo(board) -> bool:
	return any((sum(board[x::5])==-5)+(sum(board[x*5:x*5+5:])==-5)for x in range(5))

def get_res(board):
	return sum([x for x in board if x != -1])

data = open("input.txt", "r").read().split('\n\n')
input_nb = [int(x) for x in data[0].split(',')]
boards = [[int(x) for x in d.split()] for d in data[1:]]
winners = dict()
for nb in input_nb:
	boards = [[x if x != nb else -1 for x in b] for b in boards]
	for i,board in enumerate(boards):
		if is_bingo(board):
			winners[i] = get_res(board) * nb
		if (len(winners) == 100):
			print(winners[i])
			quit()