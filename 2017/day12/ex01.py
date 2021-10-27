from collections import deque

info = open('input.txt').read().splitlines()
connections = dict()
for i in info:
	number, connected_to = i.split(' <-> ')
	key = int(number)
	connected_to = [int(x) for x in connected_to.split(', ')]
	connections[key] = connected_to

q = deque()
q.append(0)
connected = set()
while q:
	key = q.popleft()
	connected.add(key)
	lst = connections[key]
	for item in lst:
		if item not in connected:
			q.append(item)

print(len(connected))