numbers = [int(i) for i in open("input.txt", "r").read().split(',')]
i = 0
numbers[1] = 12
numbers[2] = 2
while (numbers[i] != 99):
	if numbers[i] == 1:
		numbers[numbers[i + 3]] = numbers[numbers[i + 1]] + numbers[numbers[i + 2]]
	else:
		numbers[numbers[i + 3]] = numbers[numbers[i + 1]] * numbers[numbers[i + 2]]
	i += 4
print(numbers[0])