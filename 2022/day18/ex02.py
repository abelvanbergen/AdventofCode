lines = open("input.txt").read().splitlines()
lava = set()
for line in lines:
	x, y, z = [int(i) for i in line.split(',')]
	lava.add((x, y, z))

size_x = max(x for x,_,_ in lava) + 1
size_y = max(y for _,y,_ in lava) + 1
size_z = max(z for _,_,z in lava) + 1

def should_be_checked(x, y, z):
	if x < -1 or x > size_x:
		return False
	if y < -1 or y > size_y:
		return False
	if z < -1 or z > size_z:
		return False
	if (x, y, z) in visited:
		return False
	return True

def check_neighbor(coor):
	if coor in lava:
		return 1
	elif should_be_checked(*coor):
		q.add(coor)
	return 0

visited = set()
q = set()
q.add((-1, -1, -1))
sides = 0
while len(q) > 0:
	x, y, z = q.pop()
	visited.add((x, y, z))
	for d in [-1, 1]:
		sides += check_neighbor((x + d, y, z))
		sides += check_neighbor((x, y + d, z))
		sides += check_neighbor((x, y, z + d))
print(sides)

		
