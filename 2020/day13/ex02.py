x, busses = open("input.txt", "r").read().split('\n')
busses = [int(i) for i in busses.replace('x', '1').split(',')]
step = 1
i = 0
time = 0
while i < len(busses):
	if (time + i) % busses[i] == 0:
		step *= busses[i]
		i += 1
	else:
		time += step
print(time)