def get_info(line):
	coor = set()
	dis = dict()
	x = 0
	y = 0
	distance = 0
	for instruct in line:
		length = int(instruct[1:])
		if instruct[0] == 'U':
			for _ in range(length):
				y += 1
				distance += 1
				if (x, y) not in coor:
					coor.add((x, y))
					dis[(x, y)] = distance
		elif instruct[0] == 'D':
			for _ in range(length):
				y -= 1
				distance += 1
				if (x, y) not in coor:
					coor.add((x, y))
					dis[(x, y)] = distance
		elif instruct[0] == 'R':
			for _ in range(length):
				x += 1
				distance += 1
				if (x, y) not in coor:
					coor.add((x, y))
					dis[(x, y)] = distance
		elif instruct[0] == 'L':
			for _ in range(length):
				x -= 1
				distance += 1
				if (x, y) not in coor:
					coor.add((x, y))
					dis[(x, y)] = distance
		else:
			print("failure")
			print(instruct)
			quit()
	return (coor, dis)

line_1, line_2 = [x.split(',') for x in open("input.txt", "r").read().split('\n')]
coor_1, dis_1 = get_info(line_1)
coor_2, dis_2 = get_info(line_2)
answer = None
for coor in coor_1:
	if coor in coor_2:
		dis = dis_1[coor] + dis_2[coor]
		if answer is None or dis < answer:
			answer = dis
print(answer)
