numbers = [int(x) for x in open('input.txt').read().splitlines()]
amount_of_numbers = len(numbers)
format_str = "0" + str(amount_of_numbers) + "b"
lowest_amount = amount_of_numbers
for i in range(1, 2 ** amount_of_numbers):
	address = format(int(i), format_str)
	total = 0
	for i, char in enumerate(address):
		if char == "1":
			total += numbers[i]
		if (total > 150):
			break
	if (total == 150):
		if (address.count("1") < lowest_amount):
			lowest_amount = address.count("1")
print(lowest_amount)
answer = 0
for i in range(1, 2 ** amount_of_numbers):
	address = format(int(i), format_str)
	if (address.count("1") == lowest_amount):
		total = 0
		for i, char in enumerate(address):
			if char == "1":
				total += numbers[i]
			if (total > 150):
				break
		if (total == 150):
			answer += 1
print(answer)
