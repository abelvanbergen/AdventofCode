ways = 0

def count_ways(numbers, nb, end):
	global ways
	if nb == end:
		ways += 1
		return()
	if nb + 1 in numbers:
		count_ways(numbers, nb + 1, end)
	if nb + 2 in numbers:
		count_ways(numbers, nb + 2, end)
	if nb + 3 in numbers:
		count_ways(numbers, nb + 3, end)

numbers = sorted([int(i) for i in open("input.txt", "r").read().split('\n')])
res = 1
begin = 0
for i in range(len(numbers)):
	if i == len(numbers) - 1:
		ways = 0
		count_ways(numbers, begin, numbers[i])
		print(ways * res)
		quit()
	if numbers[i + 1] - numbers[i] == 3:
		ways = 0
		count_ways(numbers, begin, numbers[i])
		res = res * ways
		begin = numbers[i + 1]
