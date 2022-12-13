class Monkey:
	def __init__(self, i, data):
		self.index = i
		self.items_evaluated = 0 
		_, itemstr = data[1].split(": ")
		self.items = [int(x) for x in itemstr.split(", ")]
		tokens = data[2].split()
		self.operator = tokens[4]
		if (tokens[5] == "old"):
			self.operator_value_old = True
			self.operator_value = -1
		else:
			self.operator_value_old = False
			self.operator_value = int(tokens[5])
		self.testvalue = int(data[3].split()[3])
		self.true = int(data[4].split()[5])
		self.false = int(data[5].split()[5])
	
	def __str__(self):
		temp = "old" if self.operator_value_old else self.operator_value 
		ret = f"Monkey {self.index} -=-=-=-=-=-=-\n"
		ret += f"Items: {self.items}\n"
		ret += f"Operation: {self.operator} {temp} \n"
		ret += f"Test: divisible by {self.testvalue} ? {self.true} : {self.false}\n"
		return ret

	def get_operator_value(self, item):
		if self.operator_value_old:
			return item
		else:
			return self.operator_value

	def evaluate(self, item, monkeys):
		self.items_evaluated += 1
		if self.operator == "*":
			worry_level = (item * self.get_operator_value(item)) // 3
		else:
			worry_level = (item + self.get_operator_value(item)) // 3
		if (worry_level % self.testvalue == 0):
			monkeys[self.true].items.append(worry_level)
		else:
			monkeys[self.false].items.append(worry_level)

monkey_data = open("input.txt").read().split("\n\n")
monkeys = []
for i, m in enumerate(monkey_data):
	monkeys.append(Monkey(i, m.splitlines()))
for _ in range(20):
	for monkey in monkeys:
		for item in monkey.items:
			monkey.evaluate(item, monkeys)
		monkey.items.clear()
item_evaluations = sorted([m.items_evaluated for m in monkeys])
print(item_evaluations[-2] * item_evaluations[-1])

