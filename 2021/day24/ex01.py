class ALU:
	def __init__(self, model, instructions):
		self.model = model
		self.instructions = instructions
		self.mem = {"w":0, "x":0, "y":0, "z":0}

	def get_input(self):
		ret = self.model[0]
		self.model = self.model[1:]
		return ret

	def inp(self, key):
		self.mem[key] = int(self.get_input())

	def add(self, key, value):
		if value in "wxyz":
			self.mem[key] += self.mem[value]
		else:
			self.mem[key] += int(value)

	def	mul(self, key, value):
		if value in "wxyz":
			self.mem[key] *= self.mem[value]
		else:
			self.mem[key] *= int(value)
	
	def	div(self, key, value):
		if value in "wxyz":
			nb_to_div = self.mem[value]
		else:
			nb_to_div = int(value)
		if nb_to_div == 0:
			return False
		self.mem[key] = self.mem[key] // nb_to_div
		return True
	
	def	mod(self, key, value):
		if value in "wxyz":
			nb_to_div =  self.mem[value]
		else:
			nb_to_div =  int(value)
		if self.mem[key] < 0 or nb_to_div <= 0:
			return False
		self.mem[key] = self.mem[key] % nb_to_div
		return True

	def	eql(self, key, value):
		if value in "wxyz":
			self.mem[key] = int(self.mem[key] == self.mem[value])
		else:
			self.mem[key] = int(self.mem[key] == int(value))
	
	def run(self):
		for instruct in self.instructions:
			if instruct[0] == "inp":
				self.inp(instruct[1])
			elif instruct[0] == "add":
				self.add(instruct[1], instruct[2])
			elif instruct[0] == "mul":
				self.mul(instruct[1], instruct[2])
			elif instruct[0] == "div":
				if not self.div(instruct[1], instruct[2]):
					return False, None
			elif instruct[0] == "mod":
				if not self.mod(instruct[1], instruct[2]):
					return False, None
			elif instruct[0] == "eql":
				self.eql(instruct[1], instruct[2])
			else:
				print("unknown instruction")
				return False, None
		return True, self.mem["z"]

def is_model(index):
	return not ("0" in str(index))

def get_model(index):
	index -= 1
	while not is_model(index):
		index -= 1
	return (index)

instructions = [line.split() for line in open("input.txt").read().splitlines()]
index = 100000000000000
while True:
	index = get_model(index)
	print(index)
	alu = ALU(str(index), instructions)
	status, z = alu.run()
	if status == False:
		continue
	if z != 0:
		continue
	break
print(index)
