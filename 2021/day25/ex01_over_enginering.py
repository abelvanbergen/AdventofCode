class Cucumber:
	def __init__(self, y, x, dy, dx):
		self.y = y
		self.x = x
		self.dx = dx
		self.dy = dy

	def get_next_loc(self, max_y, max_x):
		new_y = self.y + self.dy if self.y + self.dy < max_y else 0
		new_x = self.x + self.dx if self.x + self.dx < max_x else 0
		return new_y, new_x

	def move(self, max_y, max_x):
		self.y = self.y + self.dy if self.y + self.dy < max_y else 0
		self.x = self.x + self.dx if self.x + self.dx < max_x else 0

class Sea:
	def __init__(self, grid):
		self.max_x = len(grid[0])
		self.max_y = len(grid)
		self.right = set()
		self.down = set()
		for j, line in enumerate(grid):
			for i, char in enumerate(line):
				if char == ">":
					self.right.add(Cucumber(j, i, 0, 1))
				elif char == "v":
					self.down.add(Cucumber(j, i, 1, 0))
		
	def c_can_move(self, new_y, new_x):
		for c in self.right:
			if c.x == new_x and c.y == new_y:
				return False
		for c in self.down:
			if c.x == new_x and c.y == new_y:
				return False
		return True

	def move_group(self, group):
		to_move = set()
		for c in group:
			new_y, new_x = c.get_next_loc(self.max_y, self.max_x)
			if self.c_can_move(new_y, new_x):
				to_move.add(c)
		for c in to_move:
			c.move(self.max_y, self.max_x)
		return len(to_move)

	def move(self):
		total_moved = 0
		total_moved += self.move_group(self.right)
		total_moved += self.move_group(self.down)
		return total_moved > 0

lines = open("input.txt").read().splitlines()
sea = Sea(lines)
step = 0
while sea.move():
	step += 1
	print(step)
print(step + 1)
