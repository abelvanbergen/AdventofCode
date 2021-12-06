data = open("input.txt", "r").read().split('\n\n')
input_nb = [int(x) for x in data[0].split(',')]
boards = [[int(x) for x in d.split()] for d in data[1:]]
for board in boards:
	print(board)