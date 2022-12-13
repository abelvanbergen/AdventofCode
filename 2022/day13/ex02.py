def is_smaller(left, right):
	len_left = len(left)
	len_right = len(right)
	looplen = len_left if len_left <= len_right else len_right
	for i in range(looplen):
		if type(left[i]) == int and type(right[i]) == list:
			ret = is_smaller([left[i]], right[i])
			if (ret == 0):
				continue 
			return (ret)
		if type(left[i]) == list and type(right[i]) == int:
			ret = is_smaller(left[i], [right[i]])
			if (ret == 0):
				continue 
			return (ret)
		if type(left[i]) == list and type(right[i]) == list:
			ret = is_smaller(left[i], right[i])
			if (ret == 0):
				continue 
			return (ret)
		if (left[i] < right[i]):
			return (1)
		if (left[i] > right[i]):
			return (-1)
	if (len_left < len_right):
		return (1)
	if (len_left > len_right):
		return (-1)
	return (0)

packets = [eval(x) for x in open("input.txt").read().replace("\n\n", "\n").splitlines()]
packets [*packets, [[2]], [[6]]]
changed = 1
while(changed):
	changed = 0
	for i in range(len(packets) - 1):
		if (is_smaller(packets[i], packets[i + 1]) != 1):
			packets[i], packets[i + 1] = packets[i + 1], packets[i]
			changed = 1
print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))
