line = open('input.txt').read()
group_count = 0
garbage = False
garbage_count = 0
i = 0
while i < len(line):
	if line[i] == "<" and garbage == False:
		garbage = True
	elif line[i] == "!":
		i += 1
	elif line[i] == ">" and garbage == True:
		garbage = False
	elif garbage == True:
		garbage_count += 1
	i += 1
print(garbage_count)
