def get_all_options(amount, max_value, used):
	global options
	if (amount == 2):
		for i in range(max_value + 1):
			end_list = [i, max_value - i]
			options.add(tuple(used + end_list))
	else:
		for j in range(max_value + 1):
			used.append(j)
			get_all_options(amount -1, max_value - j, used)
			used.remove(j)

def x_index(amount, char, line):
	count = 0
	i = 0
	while 1:
		if line[i] == char:
			count += 1
		if (count == amount):
			return(i)
		i += 1

def get_cal(ingredients, option):
	cal = 0
	for i in range(len(option)):
		cal += option[i] * ingredients[i][4]
	return cal

ingredients = open('input.txt').read().replace(',', '').splitlines()
amount_of_ingredients = len(ingredients)
for i, line in enumerate(ingredients):
	cap = int(line[x_index(2, ' ', line) + 1: x_index(3, ' ', line)])
	dur = int(line[x_index(4, ' ', line) + 1: x_index(5, ' ', line)])
	flavor = int(line[x_index(6, ' ', line) + 1: x_index(7, ' ', line)])
	text = int(line[x_index(8, ' ', line) + 1: x_index(9, ' ', line)])
	cal = int(line[x_index(10, ' ', line) + 1:])
	ingredients[i] = [cap, dur, flavor, text, cal]

options = set()
get_all_options(amount_of_ingredients, 100, [])
answer = 0
for option in options:
	if get_cal(ingredients, option) == 500:
		cap = 0
		dur = 0
		flavor = 0
		text = 0
		for i in range(amount_of_ingredients):
			cap += ingredients[i][0] * option[i]
			dur += ingredients[i][1] * option[i]
			flavor += ingredients[i][2] * option[i]
			text += ingredients[i][3] * option[i]
		if cap < 0 or dur < 0 or flavor < 0 or text < 0:
			total = 0
		else:
			total = cap * dur * flavor * text
		if (total > answer):
			answer = total
print(answer)