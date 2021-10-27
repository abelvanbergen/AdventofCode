alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
connecties = dict()
for char in alpha_upper:
	connecties[char] = set()

lines = [x.split(" ") for x in open("input.txt", "r").readlines()]
for line in lines:
	connecties[line[7]].add(line[1])

answer = str()
while len(answer) != 26:
	for key in connecties:
		if (len(connecties[key]) == 0):
			answer += key
			connecties[key].add("-")
			for key_2 in connecties:
				if key in connecties[key_2]:
					connecties[key_2].remove(key)
			break
print(answer)
