def get_coor(coor, line):
	x = 0
	y = 0
	for i in line:
		amount = int(i[1:])
		if 'R' in i:
			for j in range(amount):
				x += 1
				coor.add((x,y))
		elif 'L' in i:
			for j in range(amount):
				x -= 1
				coor.add((x,y))
		elif 'U' in i:
			for j in range(amount):
				y += 1
				coor.add((x,y))
		elif 'D' in i:
			for j in range(amount):
				y -= 1
				coor.add((x,y))
		else:
			print("something went wrong")
	# for i in coor:
	# 	print(i)

line_1, line_2 = open("input.txt", "r").read().split('\n')
directions_1 = line_1.split(',')
directions_2 = line_2.split(',')
coor_1 = set()
get_coor(coor_1, directions_1)
coor_2 = set()
get_coor(coor_2, directions_2)
lowest = 1000000
for coor in coor_1:
	if coor in coor_2:
		distance = abs(coor[0]) + abs(coor[1])
		if distance < lowest:
			lowest = distance
print(lowest)

