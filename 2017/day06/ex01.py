banks = [int(x) for x in open('input.txt').read().split()]
memory = set()
loop_len = 0
while 1:
	max_nb = max(banks)
	loc = banks.index(max_nb)
	banks[loc] = 0
	for i in range(loc + 1, loc + max_nb + 1):
		banks[i % len(banks)] += 1
	loop_len += 1
	if tuple(banks) in memory:
		print(loop_len)
		quit()
	memory.add(tuple(banks))
