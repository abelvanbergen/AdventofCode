dimensions = [sorted([int(j) for j in i.split('x')]) for i in open('input.txt').read().splitlines()]
answer = 0
for l, w, h in dimensions:
	answer += 2 * l + 2 * w + l * w * h
print(answer)