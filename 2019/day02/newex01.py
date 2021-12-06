numbers = [int(x) for x in open("input.txt", "r").read().split(',')]
numbers[1],numbers[2]=12,2
i = 0
while (numbers[i] != 99):
	if (numbers[i] == 1):
		numbers[i+3] = numbers[i+1] + numbers[1+2]
	else:
		numbers[i+3] = numbers[i+1] * numbers[1+2]
	i += 4
print(numbers[0])