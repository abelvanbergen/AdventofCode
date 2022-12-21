numbers = [int(x) for x in open("input.txt").read().splitlines()]
code_by_number = dict()
for i in range(len(numbers)):
	code_by_number[i] = numbers[i]
len_list = len(numbers)
list_to_move = [*range(len(numbers))]

for i in range(len(list_to_move)):
	start = list_to_move.index(i)
	to_move = code_by_number[i]
	list_to_move.pop(start)
	index = (start + to_move) % (len_list - 1)
	list_to_move.insert(index, i)
to_print = [code_by_number[n] for n in list_to_move]
index_0 = to_print.index(0)
print(sum(to_print[(index_0 + i * 1000) % len_list] for i in range(1,4)))
