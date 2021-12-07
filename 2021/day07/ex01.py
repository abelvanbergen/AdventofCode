pos = [int(x) for x in open("input.txt").read().split(',')]

def calc_distance(pos, i):
	return sum(map(lambda x: abs(x-i), pos))

dis = [0] * 2000
for i in range(2000):
	dis[i] = calc_distance(pos, i)
	if (i != 0 and dis[i] > dis[i - 1]):
		print(dis[i-1])
		quit()