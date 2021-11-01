line = open("input.txt", "r").read()[:-1]
res = 0
i = 0
while (i < len(line)):
	if (line[i] == '('):
		marker = line[i + 1:line[i:].index(')') + i:]
		lenToRepeat = int(marker[:marker.index('x')])
		amountToRepeat = int(marker[marker.index('x') + 1:])
		res += lenToRepeat * amountToRepeat
		i += len(marker) + 2 + lenToRepeat
	else:
		res += 1
		i += 1
print(res)
