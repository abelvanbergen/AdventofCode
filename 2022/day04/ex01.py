lines = open("ruben.txt").read().splitlines()
total = 0
for line in lines:
	a,b,c,d = [int(x) for x in line.replace(*",-").split("-")]
	if (a >= c and b <= d) or (c >= a and d <= b):
		total += 1
print(total)