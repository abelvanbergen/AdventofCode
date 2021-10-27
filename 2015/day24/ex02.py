def prod(lst):
	ret = 1
	for l in lst:
		ret *= l
	return ret

def get_all_options(amount, max_value, used, value_to_use):
	global options
	if (amount == 2):
		for i in value_to_use:
			if max_value - i in value_to_use and i != max_value - i and i not in used and max_value - i not in used:
				end_list = [i, max_value - i]
				options.add(tuple(used + end_list))
	else:
		for j in value_to_use:
			if j not in used:
				used.append(j)
				get_all_options(amount -1, max_value - j, used, value_to_use)
				used.remove(j)

presents = [int(x) for x in open('input.txt').read().splitlines()]
print(len(presents), sum(presents))
group_weight = sum(presents) // 4
group_size = 2
options = set()
while len(options) == 0:
	get_all_options(group_size, group_weight, [], presents)
	group_size += 1
smallest = 0
for i in options:
	QE = prod(i)
	if QE < smallest or smallest == 0:
		smallest = QE
print(smallest)