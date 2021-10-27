input_nb = 368078
# input_nb = 23
size = 1
while (size + 2)**2 < input_nb:
	size += 2
quarter = (input_nb - size**2 - 1) // (size + 1)
remainder = (input_nb - size**2) % (size + 1)
if remainder == 0:
	remainder = (size + 1)
if quarter == 0:
	x = (size + 2) // 2
	y = -((size + 2) // 2) + remainder
elif quarter == 1:
	y = (size + 2) // 2
	x = (size + 2) // 2 - remainder
elif quarter == 2:
	x = -((size + 2) // 2)
	y = (size + 2) // 2 - remainder
else:
	y = -((size + 2) // 2)
	x = -((size + 2) // 2) + remainder
print(abs(x) + abs(y))

