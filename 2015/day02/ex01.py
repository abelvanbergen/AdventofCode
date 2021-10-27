dimensions = [sorted([int(j) for j in i.split('x')]) for i in open('input.txt').read().splitlines()]
answer = 0
for l, w, h in dimensions:
	answer += 3 * l * w + 2 * w * h + 2 * l * h
print(answer)