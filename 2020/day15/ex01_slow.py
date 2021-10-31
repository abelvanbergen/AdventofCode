import sys

def list_rindex(li, x):
    for i in reversed(range(len(li))):
        if li[i] == x:
            return i

data = [int(i) for i in open(sys.argv[1], "r").read().split(',')]
lst = []
for i in data:
	lst.append(i)
for i in range(len(lst), 30000000):
	if lst[i - 1] in lst[:-1]:
		lst.append(i - 1 - list_rindex(lst[:-1], lst[i - 1]))
	else:
		lst.append(0)
print(lst[30000000 - 1])
