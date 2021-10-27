data = open('input.txt', 'r').read()
cups = [int(char) for char in data]

def get_dest_cup(cups, dest):
	while dest in (cups[0], cups[1], cups[2], cups[3]):
		dest -= 1
		if dest == 0:
			dest = 9
	return dest

for move in range(1, 101):
	new_list = list()
	dest_cup = get_dest_cup(cups, cups[0])
	i = 4
	while (cups[i - 1] != dest_cup):
		new_list.append(cups[i])
		i += 1
	new_list.append(cups[1])
	new_list.append(cups[2])
	new_list.append(cups[3])
	for j in range(i, 9):
		new_list.append(cups[j])
	new_list.append(cups[0])
	cups = new_list
answer = ""
for i in range(cups.index(1) + 1, 9):
	answer += str(cups[i])
for i in range(0, cups.index(1)):
	answer += str(cups[i])
print(answer)