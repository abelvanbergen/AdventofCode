def get_number(pos, line):
	i = 0
	count = 1
	while 1:
		while line[i] < '0'  or line[i] > '9':
			i += 1
		if count == pos:
			break
		count += 1
		while line[i] >= '0' and line[i] <= '9':
			i += 1
	j = 0
	while i + j != len(line) and (line[i + j] >= '0' and line[i + j] <= '9'):
		j += 1
	return (int(line[i:i + j]))

def more_to_do(robot):
	for key in robot:
		if len(robot[key]) == 2:
			return(1)
	return(0)

instructions = open('input.txt').read().splitlines()
robot = dict()
i = 0
robot_inst = dict()
while i < len(instructions):
	if "value" in instructions[i]:
		value = get_number(1, instructions[i])
		robot_nbr = get_number(2, instructions[i])
		if robot_nbr in robot.keys():
			robot[robot_nbr].append(value)
		else:
			robot[robot_nbr] = [value]
		instructions.remove(instructions[i])
	else:
		i += 1
for i in instructions:
	if "output" in i:
		if i.index("output") < i.index("high"):
			robot_inst[get_number(1, i)] = (get_number(2, i) + 1000, get_number(3, i))
		else:
			robot_inst[get_number(1, i)] = (get_number(2, i), get_number(3, i) + 1000)
	else:
		robot_inst[get_number(1, i)] = (get_number(2, i), get_number(3, i))
while more_to_do(robot):
	for key in robot:
		if len(robot[key]) == 2:
			nbr_1 = robot[key][0]
			nbr_2 = robot[key][1]
			if nbr_1 < nbr_2:
				robot_nbr = robot_inst[key][0]
				if robot_nbr in robot.keys():
					robot[robot_nbr].append(nbr_1)
				else:
					robot[robot_nbr] = [nbr_1]
				robot_nbr = robot_inst[key][1]
				if robot_nbr in robot.keys():
					robot[robot_nbr].append(nbr_2)
				else:
					robot[robot_nbr] = [nbr_2]
			else:
				robot_nbr = robot_inst[key][0]
				if robot_nbr in robot.keys():
					robot[robot_nbr].append(nbr_2)
				else:
					robot[robot_nbr] = [nbr_2]
				robot_nbr = robot_inst[key][1]
				if robot_nbr in robot.keys():
					robot[robot_nbr].append(nbr_1)
				else:
					robot[robot_nbr] = [nbr_1]
			robot[key] = []
			break
print(robot[1000][0] * robot[1001][0] * robot[1002][0])