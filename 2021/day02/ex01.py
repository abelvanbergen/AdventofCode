instructions = open("i", "r").read().splitlines()
x, y = 0, 0
for instruct in instructions:
	word, nb = instruct.split()
	if word == "forward":
		x += int(nb)
	elif word == "up":
		y -= int(nb)
	else:
		y += int(nb)
print(x * y)