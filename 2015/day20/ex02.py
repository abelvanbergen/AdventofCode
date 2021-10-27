import math

def amount_of_presents(number):
	commen_dividers = list()
	i = 1
	ret = 0
	while i <= math.sqrt(number):
		if (number % i == 0):
			if (number // i == i):
				if (i <= 50):
					ret += 11 * i
			else:
				if (number // i <= 50):
					ret += 11 * i
				if (i <= 50):
					ret += 11 * number // i
		i += 1
	return ret

max_presents = 29000000
increaser = 144
number = increaser
while amount_of_presents(number) < max_presents:
	number += increaser
for i in range(number - increaser, number + 1):
	if amount_of_presents(i) >= max_presents:
		print(i, amount_of_presents(i))
		quit()

# i = 0
# while i < 1000:
# 	presents = amount_of_presents(i)
# 	if (presents > highest):
# 		print(i, presents)
# 		highest = presents
# 	i += 1
