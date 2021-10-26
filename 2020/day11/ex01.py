def is_seat_availeble(seats, i, j):
	count = 0
	for k in range(0,9):
		if i + k % 3 >= 0 and i + k % 3 < len(seats[0]) and j + k // 3 >= 0 and j + k // 3 < len(seats):
			if (seats[j + (k // 3)][i + (k % 3)] == '#' and k != 4):
				count += 1
	return(count)

seats = [list(i) for i in open("input.txt", "r").read().split('\n')]
change = 1
while change > 0:
	change = 0
	occupied = 0
	temp = [row[:] for row in seats]
	for j in range(len(seats)):
		for i in range(len(seats[0])):
			ret = is_seat_availeble(seats, i - 1, j - 1)
			if seats[j][i] == 'L' and ret == 0:
				temp[j][i] = '#'
				change += 1
			elif seats[j][i] == '#' and ret >= 4:
				temp[j][i] = 'L'
				change += 1
			if temp[j][i] == '#':
				occupied += 1
	print(change)
	seats = [row[:] for row in temp]
print(occupied)
