lines = open("example.txt").read().splitlines()
x = 1
cycle = 1
res = 0
for line in lines:
	if (cycle in [20, 60, 100, 140, 180, 220]):
		res += cycle * x
	if (line[0] == 'n'):
		cycle+=1
		continue
	value = int(line.split()[1])
	cycle+=1
	if (cycle in [20, 60, 100, 140, 180,220]):
		res += cycle * x
	x += value
	cycle+=1
print(res)

