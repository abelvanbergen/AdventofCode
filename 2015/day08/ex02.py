lines = open('input.txt').read().splitlines()
total_length = sum(map(len, lines))
extended_length = 0
for line in lines:
	extended_length += 2
	for char in line:
		if char == "\\":
			extended_length += 1
		elif char == "\"":
			extended_length += 1
		extended_length += 1
print(extended_length, "-", total_length, "=", extended_length - total_length)