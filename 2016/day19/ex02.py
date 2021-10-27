input_nbr = 3014387
power = 3
while power * 3 < input_nbr:
	power *= 3
if (input_nbr // power == 1):
	print(input_nbr - power)
else:
	print(power + 2 * (input_nbr - power - power))
