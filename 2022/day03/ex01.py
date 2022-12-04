priority = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def getPriorityFromCommenChar(first, last):
	return priority.index(*(first & last))

lines = open("input.txt").read().splitlines()
print(sum(getPriorityFromCommenChar(set(x[:len(x)//2]),set(x[len(x)//2:])) for x in lines))