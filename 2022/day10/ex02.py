lines = open("input.txt").read().splitlines()
x = 1
cycle = 0
screen = ["."] * 240
for line in lines:
	if (x - (cycle % 40) in [-1, 0, 1]):
		screen[cycle] = '#'
	if (line[0] == 'n'):
		cycle+=1
		continue
	value = int(line.split()[1])
	cycle+=1
	if (x - (cycle % 40) in [-1, 0, 1]):
		screen[cycle] = '#'
	x += value
	cycle+=1
for i in range(0, 300, 40):
	print("".join(screen[i:i+40]))
