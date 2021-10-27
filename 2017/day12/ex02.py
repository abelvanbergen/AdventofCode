from collections import deque

def find_start():
	for key in connections:
		if connections[key] != -1:
			return(key)
	return(-1)

info = open('input.txt').read().splitlines()
connections = dict()
for i in info:
	number, connected_to = i.split(' <-> ')
	key = int(number)
	connected_to = [int(x) for x in connected_to.split(', ')]
	connections[key] = connected_to

groupcount = 0
while find_start() != -1:
	q = deque()
	q.append(find_start())
	connected = set()
	while q:
		key = q.popleft()
		connected.add(key)
		lst = connections[key]
		for item in lst:
			if item not in connected:
				q.append(item)
	for item in connected:
		connections[item] = -1
	groupcount += 1
print(groupcount)
