digits = open('input.txt').read()
count = 0
for i in range(len(digits)):
	if digits[i] == digits[(i + 1) % len(digits)]:
		count += int(digits[i])
print(count)