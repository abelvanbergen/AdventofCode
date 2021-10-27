path = open('input.txt').read().split(',')
x, y = 0, 0
longest_path = 0
for step in path:
	if step == "n":
		y += 1
	elif step == "s":
		y -= 1
	elif step == "ne":
		x += 1
		y += 0.5
	elif step == "se":
		x += 1
		y -= 0.5
	elif step == "nw":
		x -= 1
		y += 0.5
	else:
		x -= 1
		y -= 0.5
	dis = abs(y) - (abs(x) / 2) + abs(x)
	if dis > longest_path:
		longest_path = dis
print(longest_path)