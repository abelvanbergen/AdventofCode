number = "11011110011011101"
max_len = 35651584
while len(number) < max_len:
	rev_number = number[::-1]
	new_str = ""
	for char in rev_number:
		if char == "1":
			new_str += "0"
		else:
			new_str += "1"
	number += "0" + new_str
number = number[:max_len]
while len(number) % 2 == 0:
	i = 0
	new_nbr = ""
	while i < len(number):
		if number[i: i + 2] == "00" or number[i: i + 2] == "11":
			new_nbr += "1"
		else:
			new_nbr += "0"
		i += 2
	number = new_nbr
print(number)