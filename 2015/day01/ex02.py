level = open('input.txt').read()
answer = 0
for i, char in enumerate(level):
	if char == '(':
		answer += 1
	else:
		answer -= 1
	if answer == -1:
		print(i + 1)
		quit()