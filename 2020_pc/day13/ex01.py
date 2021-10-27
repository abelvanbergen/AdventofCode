time, busses = open("input.txt", "r").read().split('\n')
time = int(time)
busses = [int(j) for j in busses.replace('x,', '').split(',')] 
res = time
for i in busses:
	difference = (time // i + 1) * i - time
	if difference < res:
		bus = i
		res = difference
print(res * bus)