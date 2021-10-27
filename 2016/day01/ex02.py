instructions = open('input.txt').read().split(', ')
x = 0
y = 0
direction = 0
loc = set()
for i in instructions:
	if "R" in i:
		direction += 1
	else:
		direction -= 1
	if direction % 4 == 0:
		for j in range(int(i[1:])):
			y += 1
			if (x, y) not in loc:
				loc.add((x, y))
			else:
				if x < 0:
					x = -x
				if y < 0:
					y = -y
				print(x + y)
				quit()
	elif direction % 4 == 1:
		for j in range(int(i[1:])):
			x += 1
			if (x, y) not in loc:
				loc.add((x, y))
			else:
				if x < 0:
					x = -x
				if y < 0:
					y = -y
				print(x + y)
				quit()
	elif direction % 4 == 2:
		for j in range(int(i[1:])):
			y -= 1
			if (x, y) not in loc:
				loc.add((x, y))
			else:
				if x < 0:
					x = -x
				if y < 0:
					y = -y
				print(x + y)
				quit()
	else:
		for j in range(int(i[1:])):
			x -= 1
			if (x, y) not in loc:
				loc.add((x, y))
			else:
				if x < 0:
					x = -x
				if y < 0:
					y = -y
				print(x + y)
				quit()
