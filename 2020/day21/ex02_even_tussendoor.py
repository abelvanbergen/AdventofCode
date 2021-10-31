data = sorted(open('file1', 'r').read().splitlines())
answer = ""
for i in data:
	_, ing = i.split(' ')
	answer += ing + ","
print(answer[:-1])