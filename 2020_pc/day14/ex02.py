def set_all_values(number, value, mem):
	amount = number.count('X')
	format_nb = "0" + str(amount) + "b"
	for i in range(2 ** amount):
		bin_nb = format(i, format_nb)
		nb = 0
		at_x = 0
		for char in number:
			if char == 'X':
				nb = nb * 2 + int(bin_nb[at_x])
				at_x += 1
			else:
				nb = nb * 2 + int(char)
		mem[nb] = value
	return(mem)

data = open('input.txt', 'r').read().replace('mem[', '').replace(']', '').replace(' ', '').splitlines()
mem = dict()
for line in data:
	if "mask" in line:
		mask = line[5:]
	else:
		address, value = line.split('=')
		address = format(int(address), '036b')
		value = int(value)
		number = ""
		for i in range(36):
			if mask[i] == '0':
				number += address[i]
			else:
				number += mask[i]
		mem = set_all_values(number, value, mem)
print(sum(mem.values()))