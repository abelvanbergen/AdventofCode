def material_pos(material):
	if material ==  "ore": return 0
	elif material == "clay": return 1
	elif material == "obsidian": return 2
	else: return 3

class Robot:
	def __init__(self, tokens):
		self.earn = [0] * 4
		self.earn[material_pos(tokens[1])] = 1
		self.cost = [0] * 4
		for i in range(4, len(tokens), 3):
			amount = int(tokens[i])
			pos = material_pos(tokens[i+1])
			self.cost[pos] = amount
	
	def __str__(self):
		ret = "Robot -=-=-=-\n"
		ret += f"Cost: {str(self.cost)}\n"
		ret += f"Earn: {str(self.earn)}\n"
		return ret
	
	def can_be_build(self, ores):
		for i in range(4):
			if ores[i] < self.cost[i]:
				return False
		return True

	def build_robot(self, ores, active_robots):
		new_ores = [ores[i] - self.cost[i] for i in range(4)]
		new_robots = [active_robots[i] + self.earn[i] for i in range(4)]
		return new_ores, new_robots

def parse_robots(line):
	robots = []
	_,info = line.split(": ")
	for part in info[:-1].split(". "):
		robot = Robot(part.split())
		robots.append(robot)
	return robots

def collect_ores(geodes, robots):
	return [geodes[i] + robots[i] for i in range(4)]

def get_max_geodes(time, amount_ores, amount_robots):
	global states
	global times
	if (time, tuple(amount_ores), tuple(amount_robots)) in states:
		return 
	states.add((time, tuple(amount_ores), tuple(amount_robots)))
	if time <= 0:
		all_geodes.append(amount_ores[3])
		return
	for bp in robotsBluePrints:
		times += 1
		if (time == 25):
			print("25")
		if (time == 30):
			print(bp)
			# print(30)
		if bp.can_be_build(amount_ores):
			new_ores, new_robots = bp.build_robot(amount_ores, amount_robots)
			new_ores = collect_ores(new_ores, amount_robots)
			get_max_geodes(time - 1, new_ores, new_robots)
	new_ores = collect_ores(amount_ores, amount_robots)
	get_max_geodes(time - 1, new_ores, amount_robots)


total = 0

times = 0
lines = open("example.txt").read().splitlines()
for line in lines:
	all_geodes = list()
	states = set()
	amount_ores = [0, 0, 0, 0]
	amount_robots = [1, 0, 0, 0]
	robotsBluePrints = parse_robots(line)
	get_max_geodes(30, amount_ores, amount_robots)
	print(max(all_geodes))
	quit()
	


