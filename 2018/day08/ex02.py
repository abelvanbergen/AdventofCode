
def sum_metadata():
	global total_metadata
	global data
	children, metadata = data[:2]
	data = data[2:]
	value = 0
	l_value = []
	if children > 0:
		for c in range(children):
			l_value.append(sum_metadata())
		for nb in data[:metadata]:
			if nb <= len(l_value) and nb != 0:
				value += l_value[nb - 1]
	else:
		value += sum(data[:metadata])
	data = data[metadata:]
	return value

lines = open("input.txt", "r").readlines()
data = [int(x) for x in lines[0].split(' ')]
print(sum_metadata())