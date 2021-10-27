def x_index(amount, char, line):
	count = 0
	i = 0
	while 1:
		if line[i] == char:
			count += 1
		if (count == amount):
			return(i)
		i += 1

reindeer = open('input.txt').read().splitlines()
time = 2503
reindeer_info = list()
for line in reindeer:
	name = line[:line.index(' ')]
	speed = int(line[x_index(3, ' ', line) + 1: x_index(4, ' ', line)])
	time_run = int(line[x_index(6, ' ', line) + 1: x_index(7, ' ', line)])
	time_rest = int(line[x_index(13, ' ', line) + 1: x_index(14, ' ', line)])
	cycle_time = time_rest + time_run
	cycle_km = time_run * speed
	info = [name, speed, time_run, time_rest, cycle_time, cycle_km]
	reindeer_info.append(info)

reindeer_distance = dict()
reindeer_points = dict()
for reindeer in reindeer_info:
	reindeer_points[reindeer[0]] = 0
for t in range(1, time + 1):
	for reindeer in reindeer_info:
		reindeer_distance[reindeer[0]] =  (t // reindeer[4]) * reindeer[5]
		if (t % reindeer[4] >= reindeer[2]):
			reindeer_distance[reindeer[0]] +=  reindeer[5]
		else:
			reindeer_distance[reindeer[0]] +=  (t % reindeer[4]) * reindeer[1]
	max_distance = max(reindeer_distance.values())
	for i in reindeer_distance:
		if (reindeer_distance[i] == max_distance):
			reindeer_points[i] += 1

for i in reindeer_points:
	print(i, reindeer_points[i])
print(max(reindeer_points.values()))
	