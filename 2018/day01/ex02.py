num = [int(x) for x in open("input.txt", "r").readlines()]
dup = set()
answer = 0
dup.add(0)
while 1:
	for nb in num:
		answer += nb
		if answer in dup:
			print(answer)
			quit()
		dup.add(answer)