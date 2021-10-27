def is_sum(lst, value):
	for i in lst:
		if value - i in lst and i + i != value:
			return (1)
	return(0)

lst = [int(i) for i in open("input.txt", "r").read().split('\n')]
for i in range(25, len(lst)):
	if is_sum(lst[i - 25:i:], lst[i]) == 0:
		quit()
