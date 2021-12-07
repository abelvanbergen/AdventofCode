
fuel = [0] * 2000
total=0
for i in range(2000):
	total+=i
	fuel[i] = total

def sum_between(nb1, nb2):
	return(fuel[abs(nb1-nb2)])

pos = [int(x) for x in open("input.txt").read().split(',')]

def calc_distance(pos, i):
	return sum(map(lambda x: sum_between(x, i), pos))

dis = [0] * 2000
for i in range(2000):
	dis[i] = calc_distance(pos, i)
	if (i != 0 and dis[i] > dis[i - 1]):
		print(dis[i-1])
		quit()