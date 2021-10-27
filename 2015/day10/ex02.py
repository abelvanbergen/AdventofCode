def make_new_number(number):
	new_nbr = ""
	i = 1
	count = 1
	while i < len(number):
		if (number[i] == number[i - 1]):
			count += 1
		else:
			new_nbr += str(count) + number[i - 1]
			count = 1
		i += 1
	new_nbr += str(count) + number[-1]
	return new_nbr
		
number = open('input.txt').read()
for i in range(50):
	number = make_new_number(number)
print(len(number))