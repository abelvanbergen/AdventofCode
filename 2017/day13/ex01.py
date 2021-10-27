def make_pattern(depth):
	lst = list()
	for i in range(depth):
		lst.append(i)
	for i in range(depth - 2, 0, -1):
		lst.append(i)
	return(lst)

info = open('input.txt').read().splitlines()
pattern = dict()
for line in info:
	layer, depth = [int(x) for x in line.split(': ')]
	pattern[(layer, depth)] = make_pattern(depth)

answer = 0
for layer, depth in pattern:
	repeat = pattern[(layer, depth)]
	if repeat[layer % len(repeat)] == 0:
		answer += layer * depth
print(answer)