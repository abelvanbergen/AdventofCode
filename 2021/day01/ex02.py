depth = [int(x) for x in open("input.txt", "r").read().splitlines()]
lst = []
for d1, d2, d3 in zip(depth, depth[1:], depth[2:]):
	lst.append(d1 + d2 + d3)
count = 0
for d1, d2 in zip(lst, lst[1:]):
	if (d1 < d2):
		count += 1
print(count)

#shortest mode
# d=[int(x)for x in open("input.txt", "r").read().splitlines()]
# l=[x+y+z for x,y,z in zip(d, d[1:], d[2:])]
# print(sum(map(lambda x,y:x<y,l,l[1:])))