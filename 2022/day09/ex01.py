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
	for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
		if manhatten_distance(hx, hy, tx + dx, ty + dy) == 1:
			return tx + dx, ty + dy
	return tx, t

instructions = [l.split() for l in open("input.txt").read().splitlines()]
tail_loc = set()
hx,hy, tx,ty = 0, 0, 0, 0
for d, amount in instructions:
	for _ in range(int(amount)):
		if d == 'R': hx += 1
		elif d == 'L': hx -= 1
		elif d == 'U': hy += 1
		else: hy -= 1
		tx, ty = move_tail(hx, hy, tx, ty)
		tail_loc.add((tx, ty))
print(len(tail_loc))