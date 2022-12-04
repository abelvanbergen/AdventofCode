line = open("input.txt").read().splitlines()
foo_1, foo_2, x, y = line[0].split()
x_min, x_max = x.split("..")
x_min, x_max = int(x_min[2:]), int(x_max[:-1])
y_min, y_max = y.split("..")
y_min, y_max = int(y_min[2:]), int(y_max)

def land_in_tranch(dx, dy):
	y = 0
	x = 0
	while True:
		if y <= y_max and y >= y_min and x <= x_max and x >= x_min:
			return True
		if y < y_min:
			return False
		y += dy
		x += dx
		if (dx > 0):
			dx -= 1
		dy -= 1

total = 0
for dy in range(-500, 500):
	for dx in range(x_max + 1):
		if land_in_tranch(dx, dy):
			total += 1
print(total)