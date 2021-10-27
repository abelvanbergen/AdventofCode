numbers = [[int(x) for x in i.split()] for i in open('input.txt').read().splitlines()]
count = 0
for row in numbers:
	for nb in row:
		for div in row:
			if nb != div and nb % div == 0:
				count += nb // div
print(count)