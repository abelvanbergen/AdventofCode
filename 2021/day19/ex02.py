scanners_input = open("input.txt").read().split('\n\n')

class Scanner:
	def __init__(self, coors):
		self.r =  None
		self.coor = []
		self.pos = (0, 0, 0)
		self.coor.append(self.set_coor(coors))
		for r in range(1, 24):
			self.coor.append(self.get_rot_set(r))
			
	def set_coor(self, coors):
		new_set = set()
		for coor in coors:
			x, y, z = [int(c) for c in coor.split(',')]
			new_set.add((x, y, z))
		return new_set

	def get_rot_coor(self, x, y, z, r):
		rotations = [(+x,+y,+z), (+y,+z,+x), (+z,+x,+y),
					(+z,+y,-x), (+y,+x,-z), (+x,+z,-y),
					(+x,-y,-z), (+y,-z,-x), (+z,-x,-y),
					(+z,-y,+x), (+y,-x,+z), (+x,-z,+y),
					(-x,+y,-z), (-y,+z,-x), (-z,+x,-y),
					(-z,+y,+x), (-y,+x,+z), (-x,+z,+y),
					(-x,-y,+z), (-y,-z,+x), (-z,-x,+y),
					(-z,-y,-x), (-y,-x,-z), (-x,-z,-y)]
		return rotations[r]
		
	def get_rot_set(self, r):
		rotate_coor = set()
		for x, y, z in self.coor[0]:
			rotate_coor.add(self.get_rot_coor(x, y, z, r))
		return rotate_coor
	
	def get_right_rot(self):
		if self.r == None:
			return None
		return self.coor[self.r]

def get_dif_coor(c1, c2):
	return (c1[0] - c2[0], c1[1] - c2[1], c1[2] - c2[2])

scanners = []
for s in scanners_input:
	coors = s.split('\n')[1:]
	scanners.append(Scanner(coors))

def is_overlapping(scanner, base_rot):
	for i, rot in enumerate(scanner.coor):
		total = dict()
		for coor_1 in rot:
			for coor_2 in base_rot:
				d_coor = get_dif_coor(coor_2, coor_1)
				if d_coor not in total:
					total[d_coor] = 0
				total[d_coor] += 1
		if 12 in total.values():
			dx, dy, dz = 0, 0, 0
			for key in total:
				if total[key] >= 12:
					scanner.pos = key
					dx, dy, dz = key[0], key[1], key[2]
			scanner.r = i
			alligned_coor = set()
			for x, y, z in scanner.coor[i]:
				alligned_coor.add((x + dx, y + dy, z + dz))
			scanner.coor[i] = alligned_coor
			return True
	return False

scanners[0].r = 0
right_rot = [0]
wrong_rot = list(range(1, len(scanners)))

while True:
	if len(wrong_rot) == 0:
		break
	new_wrong_rot = []
	new_right_rot = [x for x in right_rot]
	for w_i in wrong_rot:
		c = 0
		for r_i in right_rot:
			if is_overlapping(scanners[w_i], scanners[r_i].get_right_rot()):
				c += 1
		if c >= 1:
			new_right_rot.append(w_i)
		else:
			new_wrong_rot.append(w_i)
	right_rot = new_right_rot
	wrong_rot = new_wrong_rot
for s in scanners:
	print(s.r)

all_scanners = []
for s in scanners:
	all_scanners.append(s.pos)

def get_manhatten_distance(a, b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])

big_distance = 0
for a in all_scanners:
	for b in all_scanners:
		dis = get_manhatten_distance(a, b)
		if dis > big_distance:
			big_distance = dis
print(big_distance)
