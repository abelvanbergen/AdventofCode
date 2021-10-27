def find_chars(persons):
	shortest_str = min(persons, key=len)
	lowest_value = 27
	for i in persons:
		count = 0
		for char in shortest_str:
			if char in i:
				count += 1
		if count < lowest_value:
			lowest_value = count
	return (lowest_value)

groups = open("input.txt", "r").read().split('\n\n')
res = 0
for i in groups:
	persons = i.split('\n')
	for j in range(len(persons)):
		persons[j] = ''.join(set(persons[j]))
	res += find_chars(persons)
print(res)