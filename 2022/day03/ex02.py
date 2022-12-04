priority = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def getPriorityFromCommenChar(first, second, third):
	return priority.index(*(first & second & third))

lines = open("input.txt").read().splitlines()
print(sum(getPriorityFromCommenChar(set(lines[i]), set(lines[i+1]), set(lines[i+2])) for i in range(0, len(lines), 3)))