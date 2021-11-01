def getLengthdecompressedLine(line):
	res = 0
	i = 0
	while (i < len(line)):
		if (line[i] == '('):
			indexEndMarker = line[i:].index(')') + i
			marker = line[i + 1:indexEndMarker:]
			lenToRepeat = int(marker[:marker.index('x')])
			amountToRepeat = int(marker[marker.index('x') + 1:])
			res += getLengthdecompressedLine(line[indexEndMarker + 1:indexEndMarker + 1 + lenToRepeat]) * amountToRepeat
			i += len(marker) + 2 + lenToRepeat
		else:
			res += 1
			i += 1
	return res

line = open("input.txt", "r").read()[:-1]
print(getLengthdecompressedLine(line))