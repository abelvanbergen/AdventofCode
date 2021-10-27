numbers = [int(x) for x in open('input.txt').read().splitlines()]
i = 0
step = 0
while i < len(numbers):
	numbers[i] += 1
	i += numbers[i] - 1
	step += 1
print(step)