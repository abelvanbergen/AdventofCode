numbers = [int(x) * 811589153 for x in open("example.txt").read().splitlines()]
code_by_number = dict()
for i in range(len(numbers)):
	code_by_number[i] = numbers[i]
len_list = len(numbers)
list_to_move = [*range(len(numbers))]
for _ in range(10):
	for i in range(len_list):
		start = list_to_move.index(i)
		to_move = code_by_number[i]
		if to_move == 0:
			continue
		list_to_move.remove(i)
		if to_move > 0:
			if to_move > len_list:
				to_move += 1
			if start < (start + to_move) % len_list:
				list_to_move.insert((start + to_move) % len_list, i)
			else:
				list_to_move.insert((start + to_move + 1) % len_list, i)
		else:
			if abs(to_move) > len_list:
				to_move -= 1
			if start > (start + to_move) % len_list:
				list_to_move.insert((start + to_move) % len_list, i)
			else:
				list_to_move.insert((start + to_move - 1) % len_list, i)
	to_print = [code_by_number[n] for n in list_to_move]
	print(to_print)
to_print = [code_by_number[n] for n in list_to_move]
index_0 = to_print.index(0)
total = 0
print(sum(to_print[(index_0 + i * 1000) % len_list] for i in range(1,4)))