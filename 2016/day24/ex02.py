from collections import deque
import math

def get_moves(node, grid):
	moves = list()
	for dx in [-1, 1]:
		if grid[node[0]][node[1] + dx] == ".":
			yield((node[0], node[1] + dx))
	for dy in [-1, 1]:
		if grid[node[0] + dy][node[1]] == ".":
			yield((node[0] + dy, node[1]))

def solve(q, end, visited):
	while q:
		depth, node =q.popleft()
		if node in visited:
			continue
		visited.add(node)
		if node == end:
			return depth
		for move in get_moves(node, grid):
			q.append((depth + 1, move))


def calc_distance(begin, end, grid):
	visited = set()
	q = deque()
	q.append((0, begin))
	return(solve(q, end, visited))

def get_lst_all_numbers(start, end):
	lst = list()
	for i in range(start, end):
		lst.append(i)
	return lst

def permute(a, l, r):
	global options
	if l==r:
		options.append(a[:])
	else: 
		for i in range(l,r+1): 
			a[l], a[i] = a[i], a[l] 
			permute(a, l+1, r) 
			a[l], a[i] = a[i], a[l]

info = open('input.txt').read().splitlines()
grid = list()
loc_num = dict()
for y, line in enumerate(info):
	row = list()
	for x, char in enumerate(line):
		if char not in ".#":
			loc_num[int(char)] = (y, x)
			row.append(".")
		else:
			row.append(char)
	grid.append(row)

distance = list()
for i in range(len(loc_num)):
	distance.append([0] * len(loc_num))
for begin in range(len(loc_num) - 1):
	for end in range(begin + 1, len(loc_num)):
		if begin != end:
			dis = calc_distance(loc_num[begin], loc_num[end], grid)
			distance[begin][end] = dis
			distance[end][begin] = dis

options = list()
lst = get_lst_all_numbers(1, len(loc_num))
permute(lst, 0, len(lst) - 1)
for o in options:
	o.insert(0, 0)
	o.append(0)
for i in options:
	print(i)
lowest = 0
for o in options:
	dis = 0
	for i in range(len(o) - 1):
		dis += distance[o[i]][o[i + 1]]
	if dis < lowest or lowest == 0:
		lowest = dis
print(lowest)
