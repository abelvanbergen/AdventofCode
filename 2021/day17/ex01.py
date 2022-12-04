line = open("input.txt").read().splitlines()
foo_1, foo_2, x, y = line[0].split()
x_min, x_max = x.split("..")
x_min, x_max = int(x_min[2:]), int(x_max[:-1])
y_min, y_max = y.split("..")
y_min, y_max = int(y_min[2:]), int(y_max)
# print(x_min, x_max, y_min, y_max)

def land_in_region(y_min, y_max, dy):
	y = 0
	while True:
		if y <= y_max and y >= y_min:
			return True
		if y < y_min:
			return False
		y += dy
		dy -= 1

def calc_highest_velocity(dy_max):
	return(sum(range(dy_max + 1)))

dy_max = 0
for dy in range(1000):
	if land_in_region(y_min, y_max, dy):
		dy_max = dy

print(calc_highest_velocity(dy_max))