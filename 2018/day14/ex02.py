input_nb = 846601
example_nb = 59414

def lstToNb(lst):
	ret = 0
	for nb in lst:
		ret = ret * 10 + nb
	return ret

def nbLen(nb):
	count = 0
	if nb == 0:
		return(1)
	while(nb > 0):
		nb = nb // 10
		count += 1
	return count

grades = [3, 7]
worker_1 = 0
worker_2 = 1
amountOfRecipes = 2
res = []
nb_len = nbLen(input_nb)
while(True):
	new_recipe = grades[worker_1] + grades[worker_2]
	for char in str(new_recipe):
		grades.append(int(char))
		if (len(grades) >= nb_len):
			nb_to_check = lstToNb(grades[len(grades) - nb_len:])
			if (nb_to_check == input_nb):
				print(len(grades) - nb_len)
				quit()
	worker_1 = (worker_1 + grades[worker_1] + 1) % len(grades)
	worker_2 = (worker_2 + grades[worker_2] + 1) % len(grades)
	# print(grades)