def	check_seat(seats, i, j, i_plus, j_plus):
	while 1:
		i += i_plus
		j += j_plus
		if (i < 0 or i >= len(seats[0]) or j < 0 or j >= len(seats)):
			return(0)
		elif (seats[j][i] == '#'):
			return(1)
		elif (seats[j][i] == 'L'):
			return(0)

def check_amount_of_seats(seats, i, j):
	res = 0
	res += check_seat(seats, i, j, -1, 0)
	res += check_seat(seats, i, j, 1, 0)
	res += check_seat(seats, i, j, 0, 1)
	res += check_seat(seats, i, j, 0, -1)
	res += check_seat(seats, i, j, 1, 1)
	res += check_seat(seats, i, j, -1, -1)
	res += check_seat(seats, i, j, 1, -1)
	res += check_seat(seats, i, j, -1, 1)
	return(res)

seats = [list(i) for i in open("input.txt", "r").read().split('\n')]
change = 1
while change > 0:
	change = 0
	occupied = 0
	temp = [row[:] for row in seats]
	for j in range(len(seats)):
		for i in range(len(seats[0])):
			ret = check_amount_of_seats(seats, i, j)
			if seats[j][i] == 'L' and ret == 0:
				temp[j][i] = '#'
				change += 1
			elif seats[j][i] == '#' and ret >= 5:
				temp[j][i] = 'L'
				change += 1
			if temp[j][i] == '#':
				occupied += 1
	seats = [row[:] for row in temp]
print(occupied)
