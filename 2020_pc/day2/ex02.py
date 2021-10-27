def is_valid_password(str):
	array = str.split(' ')
	ranges = [int(i) - 1 for i in array[0].split('-')]
	amount = array[2].count(array[1][0])
	return (array[1][0] == array[2][ranges[0]]) != (array[1][0] == array[2][ranges[1]])

print(sum(map(is_valid_password, open("input.txt", "r").read().split('\n'))))