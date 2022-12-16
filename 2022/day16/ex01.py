from copy import deepcopy

class Valve:
	def __init__(self, line):
		tokens = line.replace(",", "").split()
		self.name = tokens[1]
		self.state = False
		self.flow_rate = int(tokens[4][5:-1])
		self.neighbors = [x for x in tokens[9:]]

	def __str__(self):
		ret = f"Valve {self.name} -=-=-=-=-=-=-\n"
		ret += f"Flow rate: {self.flow_rate}\n"
		ret += f"State: {self.state}\n"
		ret += f"Neighbors: {self.neighbors}\n"
		return ret

	def __copy__(self):
		self.name

# def get_all_the_presure_scores(current_valve, all_valves, time, presurescore):
# 	if (time <= 0):
# 		all_the_presure_scores.append(presurescore)
# 		return
# 	valve = all_valves[current_valve]
# 	for n in valve.neighbors:
# 		next_valve = all_valves[n]
# 		get_all_the_presure_scores(next_valve.name, dict(all_valves), time - 1, presurescore)
# 		if (all_valves[current_valve].state == False):
# 			new_dict = dict(all_valves)
# 			new_dict[current_valve].state = True
# 			print(new_dict[current_valve].state, all_valves[current_valve].state)
# 			quit()
# 			new_presure_score = new_dict[current_valve].flow_rate * time + presurescore
# 			get_all_the_presure_scores(next_valve.name, new_dict, time - 2, new_presure_score)

valves = dict()
for line in open("example.txt").read().splitlines():
	valve = Valve(line)
	valves[valve.name] = valve

new_dict = valves.deepcopy()
new_dict["AA"].state = True
print(new_dict["AA"])
print(valves["AA"])

# current_valve = "AA"
# all_the_presure_scores = []
# get_all_the_presure_scores("AA", valves, 30, 0)
# print(all_the_presure_scores)
# print(max(all_the_presure_scores))


