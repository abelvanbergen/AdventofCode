ranges = list()
info = open('input.txt').read().splitlines()
for line in info:
	x, y = line.split('-')
	ranges.append((int(x), int(y)))
ranges = sorted(ranges)
highest = ranges[0][1]
count = 0
for i in range(1, len(ranges)):
	if ranges[i][0] - 1 <= highest:
		if ranges[i][1] > highest:
			highest = ranges[i][1]
	else:
		count += ranges[i][0] - highest - 1
		highest = ranges[i][1]
print(count)