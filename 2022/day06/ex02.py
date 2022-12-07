line = open("input.txt").read()
for i in range(len(line)):
	if (len(set(line[i:i+14])) == 14):
		print(i+14)
		break