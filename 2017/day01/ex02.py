digits = open('input.txt').read()
count = 0
half_len = len(digits) // 2
for i in range(len(digits)):
	if digits[i] == digits[(i + half_len) % len(digits)]:
		count += int(digits[i])
print(count)