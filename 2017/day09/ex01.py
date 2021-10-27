line = open('input.txt').read()
group_count = 0
garbage = False
answer = 0
i = 0
while i < len(line):
	if line[i] == "{" and garbage == False:
		group_count += 1
	elif line[i] == "!":
		i += 1
	elif line[i] == "<":
		garbage = True
	elif line[i] == ">" and garbage == True:
		garbage = False
	elif line[i] == "}" and garbage == False:
		answer += group_count
		group_count -= 1
	i += 1
print(answer)
