instructions = open("input.txt", "r").read().splitlines()
x, y, aim = 0, 0, 0
for instruct in instructions:
	word, nb = instruct.split()
	if word == "forward":
		x += int(nb)
		y += aim * int(nb)
	elif word == "up":
		aim -= int(nb)
	else:
		aim += int(nb)
print(y * x)

#shortest mode
i=open()