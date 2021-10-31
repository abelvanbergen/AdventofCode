import sys

data = [int(i) for i in open(sys.argv[1], "r").read().split(',')]
numbers = dict()
for i in range(len(data) - 1):
	numbers[data[i]] = i
last_nb = data[len(data) - 1]
for i in range(len(data) - 1, 2020):
	if last_nb in numbers:
		tem = last_nb
		last_nb = i - numbers[last_nb]
		numbers[tem] = i
	else:
		numbers[last_nb] = i
		last_nb = 0
for value, index in numbers.items():
	if index == 2020 - 1:
		print(value)