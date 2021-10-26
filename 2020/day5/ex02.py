def getnumber(nb):
	return (sum(map(lambda i: int(pow(2, 9 - i)) if (nb[i] == 'B' or nb[i] == 'R') else int(0), range(0, 10))))

passes = sorted([getnumber(i) for i in open("input.txt", "r").read().split('\n')])
for i in range(len(passes) - 1):
	if passes[i + 1] - passes [i] > 1:
		print(passes[i] + 1)