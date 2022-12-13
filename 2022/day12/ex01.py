class PriorityQueue:
	def __init__(self):
		self.queue = []
	
	def isEmpty(self):
		return len(self.queue) == 0

	def push(self, data):
		self.queue.append(data)

	def pop(self):
		if self.isEmpty():
			return None
		max_i = 0
		for i in range(len(self.queue)):
			if self.queue[i][1] < self.queue[max_i][1]:
				max_i = i
		item = self.queue[max_i]
		self.queue.remove(item)
		return item

def heuristic(a, b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_neighbors(grid, current):
	x, y = current
	for dif in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
		if (x + dif[0] < 0 or x + dif[0] >= len(grid[0])):
			continue 
		if (y + dif[1] < 0 or y + dif[1] >= len(grid)):
			continue
		if (grid[y + dif[1]][x + dif[0]] - grid[y][x] <= 1):
			yield((x + dif[0], y + dif[1]))

def dijkstra(grid, start, end):
	frontier = PriorityQueue()
	frontier.push([start, 0])
	came_from = dict()
	came_from[start] = None

	while not frontier.isEmpty():
		current, _ = frontier.pop()
		if current == end:
			break
		for n in get_neighbors(grid, current):
			if n not in came_from:
				priority = heuristic(start, end)
				frontier.push([n, priority])
				came_from[n] = current
	return came_from


lines = open("input.txt").read().splitlines()
start, end = (-1, -1), (-1,-1)
grid = []
for y, line in enumerate(lines):
	row = []
	for x, char in enumerate(line):
		if char == "S":
			start = (x, y)
			char = "a"
		elif char == "E":
			end = (x, y)
			char = "z"
		row.append((ord(char) - ord("a")))
	grid.append(row)
came_from = dijkstra(grid, start, end)
i = end
length = 1
while (came_from[i] != start):
	i = came_from[i]
	length += 1
print(length)
