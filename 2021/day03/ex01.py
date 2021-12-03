lines = open("input.txt", "r").read().splitlines()
count=[0]*len(lines[0])
for line in lines:
	for i,c in enumerate(line):
		count[i] += 1 if c == '1' else -1
print(count)
g=0
exp=len(count) - 1
for nb in count:
	if nb>0:
		g += 2**exp
	exp-=1
print(g*(2**len(count)-g-1))
