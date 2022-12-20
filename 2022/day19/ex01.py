def material_pos(material):
	match material:
		case "ore": return 0
		case "clay": return 1
		case "obsidian": return 2
		case "geode": return 3

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

def parse_robots(line):
	robots = []
	_,info = line.split(": ")
	for part in info[:-1].split(". "):
		robot = Robot(part.split())
		robots.append(robot)
	return robots

def get_max_geodes(robots_blueprints):
	robots = [1, 0, 0, 0]


total = 0
lines = open("example.txt").read().splitlines()
for line in lines:
	robots = parse_robots(line)
	for r in robots:
		print(r)
	quit()


