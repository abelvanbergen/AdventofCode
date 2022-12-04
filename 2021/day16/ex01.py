class Packet:
	def __init__(self, bi_str):
		global i
		global version_sum
		self.version = int(bi_str[i:i+3], 2)
		version_sum += self.version
		self.id = int(bi_str[i+3:i+6], 2)
		self.subpackets = []
		i += 6
		if self.id == 4:
			self.value = self.get_bi_nb(bi_str)
		else:
			if bi_str[i] == "0":
				self.total_length_subpackets = int(bi_str[i+1:i+16], 2)
				i += 16
				j = i
				while j + self.total_length_subpackets > i:
					self.subpackets.append(Packet(bi_str))
			else:
				self.number_subpackets = int(bi_str[i+1:i+12], 2)
				i += 12
				for _ in range(self.number_subpackets):
					self.subpackets.append(Packet(bi_str))

	def s_sum(self):
		return sum(p.value for p in self.subpackets)

	def s_product(self):
		ret = 1
		for p in self.subpackets:
			ret *= p.value
		return ret
	
	def s_min(self):
		return min(p.value for p in self.subpackets)
	
	def s_max(self):
		return max(p.value for p in self.subpackets)
	
	def s_gt(self):
		return int(self.subpackets[0].value > self.subpackets[1].value)
	
	def s_lt(self):
		return int(self.subpackets[0].value < self.subpackets[1].value)
	
	def s_eq(self):
		return int(self.subpackets[0].value == self.subpackets[1].value)
	
	def get_value_subpackets(self):
		if self.id == 0:
			return self.s_sum()
		elif self.id == 1:
			return self.s_product()
		elif self.id == 2:
			return self.s_min()
		elif self.id == 3:
			return self.s_max()
		elif self.id == 5:
			return self.s_gt()
		elif self.id == 6:
			return self.s_lt()
		elif self.id == 7:
			return self.s_eq()

	def __str__(self):
		ret_str = "-- Packet --\n"
		ret_str += f"version {self.version}\n"
		ret_str += f"id {self.id}\n"
		ret_str += f"value {self.value}"
		return ret_str

	def get_bi_nb(self, bi_str):
		global i
		nb_str = ""
		while True:
			nb_str += bi_str[i+1:i+5]
			if bi_str[i] == "0":
				break
			i += 5
		i += 5
		return int(nb_str, 2)

line = open("input.txt").read()[:-1]
bi_str = bin(int(line, 16))[2:]
bi_str = "0" * (4 * len(line) - len(bi_str)) + bi_str
i = 0
version_sum = 0
a = Packet(bi_str)
print(version_sum)