def calc_res(state):
	res = 0
	for i in range(len(state)):
		if state[i] == "#":
			res += i - 5
	return (res)


lines = open("input.txt", "r").readlines()
state_str = "." * 5 + lines[0][lines[0].find(":") + 2: -1] + 30 * "."
state = list()
for char in state_str:
	state.append(char)
len_state = len(state)
notes = dict()
for line in lines[2:]:
	notes[line[:5]] = line[9]
res = 0
for _ in range(100):
	new_state = ["."] * len_state
	for i in range(2, len_state - 2):
		to_check = ""
		for char in state[i - 2: i + 3:]:
			to_check += char
		if to_check in notes.keys():
			new_state[i] = notes[to_check]
	state = new_state
	old_res = res
	res = calc_res(state)
	print(calc_res(state), res, "diff: ", res - old_res)