iea, input_image_grid = open("input.txt").read().split("\n\n")
in_im = set()
dark = set()
for y, line in enumerate(input_image_grid.splitlines()):
	for x, char in enumerate(line):
		if char == "#":
			in_im.add((x, y))

def get_bin_nb(x, y):
	bin_nb = 0
	for dy in [-1, 0, 1]:
		for dx in [-1, 0, 1]:
			if (x + dx, y + dy) in in_im:
				bin_nb = bin_nb * 2 + 1
			elif (x + dx, y + dy) in dark:
				bin_nb = bin_nb * 2 + 0
			elif step % 2 == 1:
				bin_nb = bin_nb * 2 + 1
			else:
				bin_nb = bin_nb * 2 + 0
	return bin_nb

for step in range(50):
	new_image = set()
	new_dark = set()
	for c_x, c_y in in_im:
		for c_dy in [-1, 0, 1]:
			for c_dx in [-1, 0, 1]:
				if (c_x + c_dx, c_y + c_dy) in new_dark or (c_x + c_dx, c_y + c_dy) in new_image:
					continue
				index = get_bin_nb(c_x + c_dx, c_y + c_dy)
				if iea[index] == "#":
					new_image.add((c_x + c_dx, c_y + c_dy))
				else:
					new_dark.add((c_x + c_dx, c_y + c_dy))
	for c_x, c_y in dark:
		for c_dy in [-1, 0, 1]:
			for c_dx in [-1, 0, 1]:
				if (c_x + c_dx, c_y + c_dy) in new_dark or (c_x + c_dx, c_y + c_dy) in new_image:
					continue
				index = get_bin_nb(c_x + c_dx, c_y + c_dy)
				if iea[index] == "#":
					new_image.add((c_x + c_dx, c_y + c_dy))
				else:
					new_dark.add((c_x + c_dx, c_y + c_dy))
	in_im = new_image
	dark = new_dark
print(len(in_im))