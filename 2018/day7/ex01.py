alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha_example = "ABCDEF"
actions = dict()
for char in alpha_upper:
	actions[char] = set()

lines = [x.split(' ') for x in open("input.txt", "r").readlines()]
for line in lines:
	actions[line[7]].add(line[1])

answer = str()
while (len(answer) != 26):
	for key in actions:
		if (len(actions[key]) ==0):
			actions[key].add("-")
			answer += key
			for key_2 in actions:
				if key in actions[key_2]:
					actions[key_2].remove(key)
			break
print(answer)

