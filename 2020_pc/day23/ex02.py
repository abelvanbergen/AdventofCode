data = open('input.txt', 'r').read()
numbers = [int(char) for char in data]
cups = dict()
for i in range(len(numbers) - 1):
	cups[numbers[i]] = numbers[i + 1]
cups[numbers[i + 1]] = 10
for i in range(10, 1000000):
	cups[i] = i + 1
cups[1000000] = numbers[0]

def get_dest_cup(mov_cups, dest):
	while dest in mov_cups:
		dest -= 1
		if dest == 0:
			dest = 1000000
	return dest

current_cup = numbers[0]
for move in range(1, 10000001):
	ctm_1 = cups[current_cup]
	ctm_2 = cups[ctm_1]
	ctm_3 = cups[ctm_2]
	dest = get_dest_cup((current_cup, ctm_1, ctm_2, ctm_3), current_cup)
	cups[current_cup] = cups[ctm_3]
	temp = cups[dest]
	cups[dest] = ctm_1
	cups[ctm_3] = temp
	current_cup = cups[current_cup]
print(cups[1] * cups[cups[1]])