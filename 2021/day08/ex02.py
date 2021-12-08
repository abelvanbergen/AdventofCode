def decode(numbers):
	place_to_letter = ["x"] * 7
	digit_to_code = [""] * 10
	for code in numbers:
		if (len(code) == 2):
			digit_to_code[1] = code
		elif (len(code) == 3):
			digit_to_code[7] = code
		elif (len(code) == 4):
			digit_to_code[4] = code
		elif (len(code) == 7):
			digit_to_code[8] = code
	for char in digit_to_code[7]:
		if char not in digit_to_code[1]:
			place_to_letter[0] = char
	for code in numbers:
		if len(code) == 5:
			count = 0
			for char in digit_to_code[1]:
				if char in code:
					count += 1
			if count == 2:
				digit_to_code[3] = code
	for char in digit_to_code[4]:
		if char not in digit_to_code[1]:
			if char in digit_to_code[3]:
				place_to_letter[3] = char
			else:
				place_to_letter[1] = char
	for code in numbers:
		if len(code) == 6:
			count = 0
			found = digit_to_code[4] + place_to_letter[0]
			for char in found:
				if char in code:
					count += 1
			if count == 5:
				digit_to_code[9] = code
	for code in numbers:
		if len(code) == 5:
			count = 0
			for char in code:
				if char in digit_to_code[9]:
					count += 1
			if count == 4:
				print("hij vind 2")
				digit_to_code[2] = code
				if digit_to_code[1][0] in code:
					place_to_letter[2] = digit_to_code[1][0]
					place_to_letter[5] = digit_to_code[1][1]
				else:
					place_to_letter[2] = digit_to_code[1][1]
					place_to_letter[5] = digit_to_code[1][0]
	for char in digit_to_code[9]:
		if char not in place_to_letter:
			place_to_letter[6] = char
	for char in "abcdefg":
		if char not in place_to_letter:
			place_to_letter[4] = char
	return (place_to_letter)

def get_number(letters, output_value):
	total = 0
	representation = {"012456":0, "25":1, "02346":2, "02356":3, "1235":4, "01356":5, "013456":6, "025":7, "0123456":8, "012356":9}
	for nb in output_value:
		total *= 10
		new_number = []
		for char in nb:
			new_number.append(letters.index(char))
		new_number = sorted(new_number)
		str_nbr = "".join([str(x) for x in new_number])
		total += representation[str_nbr]
	return (total)

lines = open("input.txt", "r").read().splitlines()
total = 0
for line in lines:
	input_value, output_value = line.split(' | ')
	input_value = input_value.split()
	output_value = output_value.split()
	letters = decode(input_value)
	total += get_number(letters, output_value)
print(total)
