ranges = list()
info = open('input.txt').read().splitlines()
for line in info:
	x, y = line.split('-')
	ranges.append((int(x), int(y)))
ranges = sorted(ranges)
highest = ranges[0][1]
i = 1
while 1:
	if ranges[i][0] - 1 <= highest:
		if ranges[i][1] > highest:
			highest = ranges[i][1]
	else:
		print(highest + 1)
		quit()
	i += 1