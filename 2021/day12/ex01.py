lines = open("input.txt").read().splitlines()
connect = dict()
for line in lines:
	a, b = line.split('-')
	if a in connect.keys():
		connect[a].append(b)
	else:
		connect[a] = [b]
	if b in connect.keys():
		connect[b].append(a)
	else:
		connect[b] = [a]

def get_total_paths(connect, path, to_go_to):
	global total_paths
	global all_paths
	for next_loc in to_go_to:
		if next_loc.islower() and next_loc in path:
			continue
		if next_loc == "end":
			total_paths += 1
			all_paths.append(path + ["end"])
			continue
		get_total_paths(connect, path + [next_loc], connect[next_loc])

total_paths = 0
all_paths = []
get_total_paths(connect, ["start"], connect["start"])
print(total_paths)
