lst = [int(i) for i in open("input.txt", "r").read().split('\n')]
start_value = 0
end_value = 1
value = lst[start_value] + lst[end_value]
while 1:
	if value == 400480901:
		print(min(lst[start_value:end_value + 1]) + max(lst[start_value:end_value + 1]))
		quit()
	elif value > 400480901:
		value -= lst[start_value]
		start_value += 1
	else:
		end_value += 1
		value += lst[end_value]