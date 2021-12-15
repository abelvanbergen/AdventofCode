
class Intcode:
	ADD = 1
	MULTIPLY = 2
	EXIT = 99

	def __init__(self, instructions):
		self.memory = [int(x) for x in instructions.split(',')]
		self.instruction_pointer = 0
		self.stepsize = 4

	def mem_set(self, index, value):
		self.memory[index] = value

	def add(self, dest, srcs_1, srcs_2):
		self.memory[dest] = self.memory[srcs_1] + self.memory[srcs_2]

	def multiply(self, dest, srcs_1, srcs_2):
		self.memory[dest] = self.memory[srcs_1] * self.memory[srcs_2]

	def run(self):
		while (True):
			mem = self.memory[self.instruction_pointer]
			if mem == self.EXIT:
				return
			srcs_1, srcs_2, dest = self.memory[self.instruction_pointer + 1: self.instruction_pointer + 4]
			if mem == self.ADD:
				self.add(dest, srcs_1, srcs_2)
			elif mem == self.MULTIPLY:
				self.multiply(dest, srcs_1, srcs_2)
			else:
				break
			self.instruction_pointer += self.stepsize