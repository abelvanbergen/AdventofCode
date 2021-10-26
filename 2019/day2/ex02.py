def return_value(noun, ferb, numbers):
	i = 0
	print(noun, ferb)
	numbers[1] = noun
	numbers[2] = ferb
	while (numbers[i] != 99):
		if numbers[i] == 1:
			numbers[numbers[i + 3]] = numbers[numbers[i + 1]] + numbers[numbers[i + 2]]
		else:
			numbers[numbers[i + 3]] = numbers[numbers[i + 1]] * numbers[numbers[i + 2]]
		i += 4
	return(numbers[0])

numbers = [int(i) for i in open("input.txt", "r").read().split(',')]
for i in range(0, 100):
	for j in range(0, 100):
		if return_value(i, j, numbers[:]) == 19690720:
			print(100 * i + j)
			quit()