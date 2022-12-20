numbers = [int(x) for x in open("example.txt").read().splitlines()]
code_by_number = dict()
for i in range(len(numbers)):
	code_by_number[i] = numbers[i]
len_list = len(numbers)
list_to_move = [*range(len(numbers))]
for i in range(len(list_to_move)):
	print([code_by_number[n] for n in list_to_move])
	start = list_to_move.index(i)
	to_move = code_by_number[i]
	if to_move == 0:
		continue
	if to_move > 0:
		if start > (start + to_move + 1) % len_list:
			to_move += 1
		list_to_move.insert((start + to_move + 1) % len_list, i)
	else:
		if (start + to_move) % len_list == 0:
			list_to_move.append(i)
		else:
			list_to_move.insert((start + to_move) % len_list, i)
	start = start + 1 if start > (start + to_move + 1) % len_list else start
	list_to_move.pop(start)
print([code_by_number[n] for n in list_to_move])
to_print = [code_by_number[n] for n in list_to_move]
index_0 = to_print.index(0)
total = 0
print(sum(to_print[(index_0 + i * 1000) % len_list] for i in range(1,4)))
