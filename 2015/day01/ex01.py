level = open('input.txt').read()
answer = 0
for char in level:
	if char == '(':
		answer += 1
	else:
		answer -= 1
print(answer)

# one liner
# print(sum(map(lambda x:  1 if x == '(' else -1, open('input.txt').read())))