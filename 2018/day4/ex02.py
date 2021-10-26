def is_oldest_date(date_1, date_2):
	numbers_1 = [int(x) for x in date_1.split(" ")]
	numbers_2 = [int(x) for x in date_2.split(" ")]
	for i in range(5):
		if (numbers_1[i] != numbers_2[i]):
			if (numbers_1[i] > numbers_2[i]):
				return (1)
			else:
				return (0)



data = open("input.txt", "r").read().replace("-", " ").replace(":", " ").split("\n")
for datum in data:
	change = 1
	while change == 1:
		change = 0
		for i in range(len(data) - 1):
			if is_oldest_date(data[i][1:data[i].find(']'):], data[i + 1][1:data[i + 1].find(']'):]) == 1:
				temp = data[i]
				data[i] = data[i + 1]
				data[i + 1] = temp
				change = 1
guards = set()
time_sleep = dict()
for i, datum in enumerate(data):
	info = datum.split(" ")
	if "Guard" in datum:
		for inf in info:
			if inf[0] == "#":
				current_guard = int(inf[1:])
	elif "wakes" in datum:
		info_2 = data[i - 1].split(" ")
		time_1, time_2 = int(info[4][:-1:]), int(info_2[4][:-1:])
		if current_guard not in time_sleep.keys():
			time_sleep[current_guard] = [0] * 60
		for i in range(time_2, time_1):
			time_sleep[current_guard][i] += 1
for guard in time_sleep:
	print(guard, time_sleep[guard])
most_times = 0
loc = 0
guard = 0
for g in time_sleep:
	rithm = time_sleep[g]
	for i in range(len(rithm)):
		if rithm[i] > most_times:
			most_times = rithm[i]
			loc = i
			guard = g
print(most_times)
print(loc, "*", guard, "=", loc * guard)

