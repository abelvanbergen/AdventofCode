
class Intcode:
	ADD = 1
	MULTIPLY = 2
	SAVE_INPUT = 3
	GIVE_OUTPUT = 4
	EXIT = 99

	def __init__(self, instructions):
		self.memory = [int(x) for x in instructions.split(',')]
		self.instruction_pointer = 0
		self.stepsize = 4

	def get_value_in_mode(mem, par1, par2, par3, mode):
		mem = "0" * (5 - len(str(mem))) + str(mem)
		par1 = self.memory[par1] if mem[2] == "0" else par1
		par2 = self.memory[par2] if mem[1] == "0" else par2
		par3 = self.memory[par3] if mem[0] == "0" else par3
		return par1, par2, par3
	
	def mem_set(self, index, value):
		self.memory[index] = value

	def add(self, mem, srcs_1, srcs_2, dest):
		self.memory[dest] = self.memory[srcs_1] + self.memory[srcs_2]

	def multiply(self, mem, par1, par2, par3:
		srcs_1, srcs_1
		self.memory[dest] = self.memory[srcs_1] * self.memory[srcs_2]

	def run(self):
		while (True):
			mem = self.memory[self.instruction_pointer]
			p
			if mem == self.EXIT:
				return
			srcs_1, srcs_2, dest = self.memory[self.instruction_pointer + 1: self.instruction_pointer + 4]
			if mem == self.ADD:
				self.add(dest, srcs_1, srcs_2)
			elif mem == self.MULTIPLY:
				self.multiply(dest, srcs_1, srcs_2)
			elif mem == self.MULTIPLY:
				self.multiply(dest, srcs_1, srcs_2)
			elif mem == self.MULTIPLY:
				self.multiply(dest, srcs_1, srcs_2)
			else:
				break
			self.instruction_pointer += self.stepsize