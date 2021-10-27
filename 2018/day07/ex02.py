alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha_example = "ABCDEF"
amount_of_workers = 5
connecties = dict()
for i, char in enumerate(alpha_upper):
	connecties[char] = [i + 1 + 60, set()]

lines = [x.split(" ") for x in open("input.txt", "r").readlines()]
for line in lines:
	connecties[line[7]][1].add(line[1])

workers = set()
answer = str()
keys_to_remove = set()
i = 0
while (len(answer) != len(alpha_upper)):
	for key in connecties:
		if len(connecties[key][1]) == 0 and (len(workers) < amount_of_workers or key in workers):
			workers.add(key)
			connecties[key][0] -= 1
			if (connecties[key][0] == 0):
				answer += key
				connecties[key][1].add("-")
				keys_to_remove.add(key)
	for key in keys_to_remove:
		workers.remove(key)
		for key_2 in connecties:
					if key in connecties[key_2][1]:
						connecties[key_2][1].remove(key)
	keys_to_remove.clear()
	i += 1
print(i)