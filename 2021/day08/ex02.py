
def decode(values):
	letter_to_value = ["x"] * 7
	letter_in_value = dict()
	unique_letters = {len(l):l for l in values if len(l) in [2, 3, 4, 7]}
	for key in unique_letters:
		value = unique_letters[key]
		if len(value) == 2:
			letter_in_value[1] = value
		elif len(value) == 3:
			letter_in_value[7] = value
		elif len(value) == 4:
			letter_in_value[4] = value
		elif len(value) == 7:
			letter_in_value[8] = value

	while (letter_to_value.count("x") != 0):
		print(letter_to_value)
		if 2 in letter_in_value.keys() and 3 in letter_in_value.keys():
			for char in letter_in_value[3]:
				if char not in letter_in_value[2]:
					letter_to_value[0] = char
		for value in values:
			if len(value) == 5 and 2 in unique_letters.keys():
				count = 0
				for char in unique_letters[2]:
					if char in value:
						count += 1
				if count == 2:
					letter_in_value[3] = value
		for value in values:
			if len(value) == 6 and 3 in letter_in_value.keys():
				count = 0
				for char in value:
					if char in letter_in_value[3]:
						count += 1
				if count == 5:
					letter_in_value[6] = value
		for value in values:
			if len(value) == 5 and 6 in letter_in_value.keys():
				count = 0
				for char in value:
					if char in letter_in_value[6]:
						count += 1
				if count == 5:
					letter_in_value[5] = value
		if 2 in letter_in_value.keys() and 3 in letter_in_value.keys() and 4 in letter_in_value.keys():
			for char in letter_in_value[4]:
				if char in letter_in_value[3] and char not in letter_in_value[2]:
					letter_to_value[3] = char
				if char not in letter_in_value[3]:
					letter_to_value[1] = char
		if letter_to_value[3] != "x":
			for value in values:
				if len(value) == 8:
					if letter_to_value[3] not in value:
						letter_in_value[0] = value
		if letter_in_value[1] != "x":
			for value in values:
				if len(value) == 5 and letter_in_value[1] in value:
					letter_in_value[5] = value
		if 5 in letter_in_value.keys() and 1 in letter_in_value.keys():
			if letter_in_value[1][0] in letter_in_value[5]:
				letter_to_value[5] = letter_in_value[1][0]
				letter_to_value[2] = letter_in_value[1][1]
			else:
				letter_to_value[5] = letter_in_value[1][1]
				letter_to_value[2] = letter_in_value[1][0]
		for value in values:
			if len(value) == 6:
				count = 0
				for char in value:
					if char in  letter_to_value:
						count += 1
				if count == 5:
					for char in value:
						if char not in letter_to_value:
							letter_to_value[6] = char
		if letter_to_value.count("x") == 1:
			for char in "abcdefg":
				if char not in letter_to_value:
					letter_to_value[letter_to_value.index('x')] = char
	return (letter_to_value)

lines = open("e", "r").read().splitlines()
for line in lines:
	input_value, output_value = line.split(' | ')
	input_value = input_value.split()
	output_value = output_value.split()
	all_values = output_value + input_value
	print(all_values)
	letters = decode(all_values)
	print("hij komt er ooit uit")
	print(letters)
	quit()

