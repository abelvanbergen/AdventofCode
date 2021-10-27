#exercise 1 max range = 2017 and item_after = 2017
#exercise 2 max_range = 50000000 and item_after = 0

from collections import deque

puzzle = 348
max_range = 50000000
item_after = 0
spinlock = deque([0])
for i in range(1, max_range + 1):
	spinlock.rotate(-puzzle)
	spinlock.append(i)
	print(spinlock)

print(spinlock[spinlock.index(item_after) + 1])