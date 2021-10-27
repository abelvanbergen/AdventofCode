info, your_ticket, other_ticket = open('input.txt', 'r').read().split('\n\n')
info = [i[i.index(':') + 2:] for i in info.split('\n')]
boarder = set()
for i in info:
	value = i.split(" or ")
	for j in value:
		min, max, = j.split("-")
		min, max = int(min), int(max)
		for k in range(min, max + 1):
			boarder.add(k)
other_ticket = other_ticket[1:].split('\n')
res = 0
for i in other_ticket[1:]:
	nb = [int(j) for j in i.split(',')]
	for j in nb:
		if not j in boarder:
			res += 1
			break
print(len(boarder))
print(res)