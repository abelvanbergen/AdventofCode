class Coor:
	def __init__(self, c):
		self._min = c[0]
		self._max = c[1]

	def is_overlapping(self, coor):
		if self._min > coor._max:
			return False, None
		if self._max < coor._min:
			return False, None
		o_min = coor._min if self._min < coor._min else self._min
		o_max = coor._max if self._max > coor._max else self._max
		return True, (o_min, o_max)

	def get_length(self):
		return (self._max - self._min + 1)

	def _print(self):
		print(self._min, self._max)

class Beam:
	def __init__(self, coor):
		self.x = Coor(coor[0])
		self.y = Coor(coor[1])
		self.z = Coor(coor[2])

	def is_overlapping(self, beam):
		is_overlapping, x = self.x.is_overlapping(beam.x)
		if not is_overlapping:
			return False, None
		is_overlapping, y = self.y.is_overlapping(beam.y)
		if not is_overlapping:
			return False, None
		is_overlapping, z = self.z.is_overlapping(beam.z)
		if not is_overlapping:
			return False, None
		return True, Beam((x, y, z))

	def calc_volume(self):
		len_x = self.x.get_length()
		len_y = self.y.get_length()
		len_z = self.z.get_length()
		return (len_x * len_y * len_z)

	def _print(self):
		print("-- X --")
		self.x._print()
		print("-- Y --")
		self.y._print()
		print("-- Z --")
		self.z._print()

instructions = open("input.txt").read().splitlines()
reactor_on = set()
reactor_off = set()
i = 0
for line in instructions:
	status, coors = line.split()
	x_s, y_s, z_s = coors.split(',')
	x = tuple(int(nb) for nb in x_s[2:].split(".."))
	y = tuple(int(nb) for nb in y_s[2:].split(".."))
	z = tuple(int(nb) for nb in z_s[2:].split(".."))
	new_beam = Beam((x, y, z))
	if status == "on":
		temp = set()
		for b in reactor_on:
			is_overlapping, o_beam = b.is_overlapping(new_beam)
			if is_overlapping:
				temp.add(o_beam)
		for b in reactor_off:
			is_overlapping, o_beam = b.is_overlapping(new_beam)
			if is_overlapping:
				reactor_on.add(o_beam)
		for b in temp:
			reactor_off.add(b)
		reactor_on.add(new_beam)
	else:
		temp = set()
		for b in reactor_off:
			is_overlapping, o_beam = b.is_overlapping(new_beam)
			if is_overlapping:
				temp.add(o_beam)
		for b in reactor_on:
			is_overlapping, o_beam = b.is_overlapping(new_beam)
			if is_overlapping:
				reactor_off.add(o_beam)
		for b in temp:
			reactor_on.add(b)
	# new_reactor_on = set()
	# for b in reactor_on:
	# 	if b in reactor_off:
	# 		reactor_off.remove(b)
	# 	else:
	# 		new_reactor_on.add(b)
	# reactor_on = new_reactor_on
volume = 0
for b in reactor_on:
	volume += b.calc_volume()
for b in reactor_off:
	volume -= b.calc_volume()
print(volume)