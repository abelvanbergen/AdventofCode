grid = [[int(x) for x in l] for l in open("input.txt").read().splitlines()]
grid_max_x = len(grid[0])
grid_max_y = len(grid)


class priorityQueue:
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

def calc_prio(grid, x, y):
	return x + y

def get_all_neighbours(x, y):
	neighbors = []
	for dx, dy in [(-1, 0), (0, -1)]:
		if x + dx < 0 or x + dx >= grid_max_x:
			continue
		if y + dy < 0 or y + dy >= grid_max_y:
			continue
		neighbors.append((x + dx, y + dy))
	return neighbors

q = priorityQueue()
q.push(((len(grid[0]) - 1, len(grid) - 1), 0))
cost_so_far = dict()
cost_so_far[(len(grid[0]) - 1, len(grid) - 1)] = grid[len(grid) - 1][len(grid[0]) - 1]

while not q.isEmpty():
	c_coor, prio = q.pop()
	x, y = c_coor
	if c_coor == (0, 0):
		break 
	
	for n_x, n_y in get_all_neighbours(x, y):
		new_cost = cost_so_far[c_coor] + grid[n_y][n_x]
		if (n_x, n_y) not in cost_so_far or new_cost < cost_so_far[(n_x, n_y)]:
			cost_so_far[(n_x, n_y)] = new_cost
			prio = new_cost + calc_prio(grid, n_x, n_y)
			q.push(((n_x, n_y), prio))

print(cost_so_far[(0, 0)] - grid[0][0])