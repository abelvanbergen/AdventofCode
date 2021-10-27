data = open('input.txt', 'r').read().replace('mem[', '').replace(']', '').replace(' ', '').split('\n')
mem = dict()
for i in data:
	if "mask" in i:
		mask = i[5:]
	else:
		address, value = i.split('=')
		address = int(address)
		value = bin(int(value))[2:]
		nb = 0
		for i in range(36 - len(value)):
			if (mask[i] == 'X'):
				nb = nb * 2 + 0
			else:
				nb = nb * 2 + int(mask[i])
		i = 36 - len(value)
		for char in value:
			if mask[i] == 'X':
				nb = nb * 2 + int(char)
			else:
				nb = nb * 2 + int(mask[i])
			i += 1
		mem[address] = nb
print(sum(mem.values()))