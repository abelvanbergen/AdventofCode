numbers = sorted([int(i) for i in open("input.txt", "r").read().split('\n')])
prev = 0
one_count = 0
three_count = 1
for i in numbers:
	if i - prev == 1:
		one_count += 1
	elif i - prev == 3:
		three_count += 1
	prev = i
print(one_count, '*', three_count, "=", one_count * three_count)