def getnumber(nb):
	return (sum(map(lambda i: int(pow(2, 9 - i)) if (nb[i] == 'B' or nb[i] == 'R') else int(0), range(0, 10))))

print(max([getnumber(i) for i in open("input.txt", "r").read().split('\n')]))