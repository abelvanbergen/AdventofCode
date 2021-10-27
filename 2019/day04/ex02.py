doub = ["00", "11", "22", "33", "44", "55", "66", "77", "88", "99"]
trip = ["000", "111", "222", "333", "444", "555", "666", "777", "888", "999"]
answer = 0
for nb in range(145852, 616942):
	nb_str = str(nb)
	for index, double in enumerate(doub):
		if double in nb_str and trip[index] not in nb_str:
			test = 0
			for i in range(len(nb_str) - 1):
				if int(nb_str[i]) > int(nb_str[i + 1]):
					test = 1
			if test == 0:
				print(nb_str)
				answer += 1
			break
print(answer)
