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

pairs = [x.splitlines() for x in open("input.txt").read().split('\n\n')]
count = 0
for i, item in enumerate(pairs, 1):
	left = eval(item[0])
	right = eval(item[1])
	count += i if is_smaller(left, right) == 1 else 0
print(count)
