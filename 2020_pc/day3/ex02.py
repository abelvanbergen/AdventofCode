import math
array = open("input.txt", "r").read().split('\n')
step = [[1,1], [3,1], [5,1], [7,1], [1,2]]
res = [0] * 5
for k in range(5):
	for i in range(0, len(array) // step[k][1]):
		res[k] += array[i * step[k][1]][(i * step[k][0]) % len(array[1])] == '#'
print(math.prod(res))			