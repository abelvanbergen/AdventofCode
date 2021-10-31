# import sys

# data = [int(i) for i in open(sys.argv[1], "r").read().split(',')]
# numbers = dict()
# for i in range(len(data) - 1):
# 	numbers[data[i]] = i
# last_nb = data[len(data) - 1]
# for i in range(len(data) - 1, 30000000 - 1):
# 	if last_nb in numbers:
# 		numbers[last_nb], last_nb = i, i - numbers[last_nb]
# 	else:
# 		numbers[last_nb], last_nb  = i, 0
# print(last_nb)

nbs = [int(x) for x in open('input.txt', 'r').read().split(',')]
d = dict()
for i in range(len(nbs) - 1):
	d[nbs[i]] = i
val = nbs[-1]
for i in range(len(nbs) - 1, 30000000 - 1):
	if val in d:
		d[val], val = i, i - d[val]
	else:
		# val, d[val] = 0, i
 		d[val], val = i, 0
print(val)