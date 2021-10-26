instruct = open("input.txt", "r").readlines()
answer = 0
for instruct in instruct:
	answer += int(instruct)
print(answer)

#one-liner
# print(sum([int(x) for x in open("input.txt", "r").readlines()]))