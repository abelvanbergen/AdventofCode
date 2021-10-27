def get_number(pos, line):
	i = 0
	count = 1
	while 1:
		while line[i] < '0'  or line[i] > '9':
			i += 1
		if count == pos:
			break
		count += 1
		while line[i] >= '0' and line[i] <= '9':
			i += 1
	j = 0
	while i + j != len(line) and (line[i + j] >= '0' and line[i + j] <= '9'):
		j += 1
	return (int(line[i:i + j]))

def get_weight(key):
	if key not in connect.keys():
		return(weight[key])
	else:
		lst = connect[key]
		weight_first_node = get_weight(lst[0])
		for i, item in enumerate(lst[1:]):
			if get_weight(item) != weight_first_node:
				if i == 0:
					if weight_first_node != get_weight(lst[2]):
						print(weight[lst[0]] + get_weight(lst[1]) - weight_first_node)
						quit()
					else:
						print(weight[lst[1]] + weight_first_node - get_weight(lst[1]))
						quit()
				else:
					print(weight[item] + weight_first_node - get_weight(item))
					quit()
		return(len(lst) * weight_first_node + weight[key])

lines = [i.split(' -> ') for i in open('input.txt').read().splitlines()]
weight = dict()
for line in lines:
	weight[line[0][:line[0].index(' ')]] = get_number(1, line[0])
connect = dict()
for line in lines:
	if len(line) == 2:
		key, connected_to = line
		key = key[:key.index(' ')]
		connected_to = connected_to.split(', ')
		connect[key] = connected_to
get_weight('vvsvez')
