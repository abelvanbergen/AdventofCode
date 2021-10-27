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
			time_sleep[current_guard] = 0
		time_sleep[current_guard] += time_1 - time_2
guard_most_asleep = 0
minutes_asleep = 0
which_minutes_asleep = [0] * 60
for key in time_sleep:
	if time_sleep[key] > minutes_asleep:
		guard_most_asleep = key
		minutes_asleep = time_sleep[key]
for i, datum in enumerate(data):
	info = datum.split(" ")
	if "Guard" in datum:
		for inf in info:
			if inf[0] == "#":
				current_guard = int(inf[1:])
	elif "wakes" in datum and current_guard == guard_most_asleep:
		info_2 = data[i - 1].split(" ")
		time_1, time_2 = int(info[4][:-1:]), int(info_2[4][:-1:])
		for i in range(time_2, time_1):
			which_minutes_asleep[i] += 1
print(guard_most_asleep)
most_times = 0
loc = 0
for i in range(len(which_minutes_asleep)):
	if which_minutes_asleep[i] > most_times:
		most_times = which_minutes_asleep[i]
		loc = i
print(loc * guard_most_asleep)
