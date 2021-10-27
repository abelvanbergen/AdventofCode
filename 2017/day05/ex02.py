numbers = [int(x) for x in open('input.txt').read().splitlines()]
i = 0
step = 0
while i < len(numbers):
	old_i = i
	i += numbers[i]
	if numbers[old_i] >= 3:
		numbers[old_i] -= 1
	else:
		numbers[old_i] += 1
	step += 1
print(step)