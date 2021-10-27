def  difference(str_1, str_2):
	count = 0
	for i in range(len(str_1)):
		if str_1[i] != str_2[i]:
			count += 1
	return (count)

IDs = open("input.txt", "r").readlines()
for ID_1 in IDs:
	for ID_2 in IDs:
		if (difference(ID_1, ID_2) == 1):
			for i in range(len(ID_1)):
				if ID_1[i] == ID_2[i]:
					print(ID_1[i], end='')
			quit()

			
