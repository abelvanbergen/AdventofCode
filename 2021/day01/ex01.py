depth = [int(x) for x in open("input.txt", "r").read().splitlines()]
count = 0
for d1, d2 in zip(depth, depth[1:]):
	if (d1 < d2):
		count += 1
print(count)