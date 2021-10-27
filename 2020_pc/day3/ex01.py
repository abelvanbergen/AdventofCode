array = open("input.txt", "r").read().split('\n')
count = 0
for i in range(len(array)):
	count += array[i][(i * 3) % len(array[0])] == '#'
print(count)