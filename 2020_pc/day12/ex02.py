instructions = open("input.txt", "r").read().split('\n')
ship_x = 0
ship_y = 0
wayp_x = 10
wayp_y = 1
for i in instructions:
	if "N" in i:
		wayp_y += int(i[1:])
	elif "E" in i:
		wayp_x += int(i[1:])
	elif "S" in i:
		wayp_y -= int(i[1:])
	elif "W" in i:
		wayp_x -= int(i[1:])
	elif "R" in i:
		amount = int(i[1:]) // 90
		for j in range(amount):
			temp = wayp_y
			wayp_y = wayp_x * -1
			wayp_x = temp
	elif "L" in i:
		amount = int(i[1:]) // 90
		for j in range(amount):
			temp = wayp_y
			wayp_y = wayp_x
			wayp_x = temp * -1
	else:
		ship_x += int(i[1:]) * wayp_x
		ship_y += int(i[1:]) * wayp_y
	print("wayp_x:", wayp_x, "wayp_y:", wayp_y)
	print("wayp_x:", wayp_x, "wayp_y:", wayp_y)
print(abs(ship_x) + abs(ship_y))