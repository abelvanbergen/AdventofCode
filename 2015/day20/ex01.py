import math

def amount_of_presents(number):
	commen_dividers = list()
	i = 1
	ret = 0
	while i <= math.sqrt(number):
		if (number % i == 0):
			if (number // i == i):
				ret += 10 * i
			else:
				ret += 10 * i + 10 * number // i
		i += 1
	return ret

max_presents = 29000000
increaser = 1728
number = increaser
while amount_of_presents(number) < max_presents:
	number += increaser
for i in range(number - increaser, number + 1):
	if amount_of_presents(i) >= max_presents:
		print(i)
		quit()
