input_nb = 846601
example_nb = 5

def lstToNb(lst):
	ret = 0
	for nb in lst:
		ret = ret * 10 + nb
	return ret

grades = [3, 7]
worker_1 = 0
worker_2 = 1
amountOfRecipes = 2
res = []
while(True):
	new_recipe = grades[worker_1] + grades[worker_2]
	for char in str(new_recipe):
		if amountOfRecipes >= input_nb:
			res.append(int(char))
			if len(res) == 10:
				print(lstToNb(res))
				quit()
		grades.append(int(char))
		amountOfRecipes+= 1
	worker_1 = (worker_1 + grades[worker_1] + 1) % len(grades)
	worker_2 = (worker_2 + grades[worker_2] + 1) % len(grades)
	# print(grades)