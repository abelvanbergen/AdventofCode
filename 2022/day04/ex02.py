lines = open("input.txt").read().splitlines()
total = 0
for line in lines:
	a,b,c,d = [int(x) for x in line.replace(*",-").split("-")]
	if (c <= a <= d) or (a <= c <= b):
		total += 1
print(total)

