def is_valid_password(str):
	ranges, char, password = str.replace(':', '').split(' ')
	min_range, max_range = [int(i) for i in ranges.split('-')]
	amount = password.count(char)
	return (amount >= min_range and amount <= max_range)

print(sum(map(is_valid_password, open("input.txt", "r").read().split('\n'))))
