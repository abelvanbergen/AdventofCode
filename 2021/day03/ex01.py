def bi_to_dec(nb):
	res = 0
	exp = 0
	for i in range(len(nb) - 1, -1, -1):
		if nb[i] == 1:
			res += 2**exp
		exp+=1
	return (res)


bi_nb = open("input.txt", "r").read().splitlines()
gamma = [0]* len(bi_nb[0])
epsilon = [0] * len(bi_nb[0])
for i in range(len(bi_nb[0])):
	count = 0
	for j in range(len(bi_nb)):
		if bi_nb[j][i] == '1':
			count += 1
	if 2*count>len(bi_nb):
		gamma[i] = 1
	else:
		epsilon[i] = 1
print(bi_to_dec(gamma) * bi_to_dec(epsilon))