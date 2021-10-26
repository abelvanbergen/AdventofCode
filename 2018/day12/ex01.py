# lines = open("input.txt", "r").readlines()
# state_str = "." * 5 + lines[0][lines[0].find(":") + 2: -1] + 30 * "."
# state = list()
# for char in state_str:
# 	state.append(char)
# len_state = len(state)
# notes = dict()
# for line in lines[2:]:
# 	notes[line[:5]] = line[9]

# for _ in range(20):
# 	new_state = ["."] * len_state
# 	for i in range(2, len_state - 2):
# 		to_check = ""
# 		for char in state[i - 2: i + 3:]:
# 			to_check += char
# 		if to_check in notes.keys():
# 			new_state[i] = notes[to_check]
# 	state = new_state
# 	print(state)

# res = 0
# for i in range(len(state)):
# 	if state[i] == "#":
# 		res += i - 5
# print(res)

# i = 0
# for _ in range(50000000000):
# 	i += 1
# print("done")


lst = [2, 5, 8, 3, 4, 8, 5, 7, 1, 0, 3]

def get_nb(element):
	if (type(element) == list):
		return(sum([get_nb(x) for x in lst]))
	if (type(element) == int)
		return(elemnt)
	return (-sys.maxsize)

def average(lst):
	return (sum(lst) / len(lst)))

def count_uneven(lst):
	return (sum(map(lambda x: 1 if x % 2 == 1 else 0, lst)))

def sum_lst(lst):
	return (sum(lst))

def max_value(lst):
	return (max(lst))

def min_value(lst):
	return (min(lst))



print(count_uneven(lst))
