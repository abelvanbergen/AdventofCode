state, instructions = [l.split('\n') for l in open("input.txt").read().split('\n\n')]
stacks = [[] for _ in state[-1].split()]
for line in state[-2::-1]:
	j = 0
	for i in range(1,len(line),4):
		if (line[i] != ' '):
			stacks[j].append(line[i])
		j += 1
for line in instructions[:-1]:
	tokens = line.split()
	amount, src, dest = [int(tokens[i]) for i in range(1,len(tokens), 2)]
	stacks[dest-1] += stacks[src-1][-amount:]
	stacks[src-1] = stacks[src-1][:-amount]
print("".join(x[-1] for x in stacks))