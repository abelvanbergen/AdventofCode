#ex01 how many save tiles in 40 rows
#ex02 how many save tiles in 400000 rows

grid = []
first_row = open('input.txt').read()
grid.append(first_row)
for j in range(1, 400000):
	row = ""
	for i in range(len(grid[0])):
		if i == 0:
			left = "."
		else:
			left = grid[j - 1][i - 1]
		middle = grid[j - 1][i]
		if i == len(grid[0]) - 1:
			right = "."
		else:
			right = grid[j - 1][i + 1]
		if [left, middle, right] in [["^", ".", "."], ["^", "^", "."], [".", "^", "^"], [".", ".", "^"]]:
			row += "^"
		else:
			row += "."
	grid.append(row)
count = 0
for row in grid:
	count += row.count(".")
print(count)