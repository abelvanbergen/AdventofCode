def manhatten_distance(ax, ay, bx, by):
	return (abs(ax - bx) + abs(ay - by))

def move_tail(hx, hy, tx, ty):
	if (hx == tx):
		if hy - ty in [-1, 0, 1]:
			return tx, ty
		if (hy > ty):
			ty += 1
		else:
			ty -= 1
		return tx, ty
	if (hy == ty):
		if hx - tx in [-1, 0, 1]:
			return tx, ty
		if (hx > tx):
			tx += 1
		else:
			tx -= 1
		return tx, ty
	for dx, dy in [(2, 2), (2, -2), (-2, 2), (-2, -2)]:
		if (hx, hy) == (tx + dx, ty + dy):
			return tx + dx//2, ty + dy//2
	for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
		if manhatten_distance(hx, hy, tx + dx, ty + dy) == 1:
			return tx + dx, ty + dy
	return tx, ty

instructions = [l.split() for l in open("input.txt").read().splitlines()]
tail_loc = set()
knots = [[0, 0] for _ in range(10)]
for d, amount in instructions:
	for _ in range(int(amount)):
		if d == 'R': knots[0][0] += 1
		elif d == 'L': knots[0][0] -= 1
		elif d == 'U': knots[0][1] += 1
		else: knots[0][1] -= 1
		for i in range(1, 10):
			knots[i][0], knots[i][1] = move_tail(knots[i - 1][0], knots[i - 1][1], knots[i][0], knots[i][1])
		tail_loc.add(tuple(knots[9]))
print(len(tail_loc))