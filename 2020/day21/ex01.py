items = open('input.txt', 'r').read().replace(')', '').splitlines()
ingredients = list()
allergens = list()
for line in items:
	ingredient, allergen = line.split(' (contains ')
	ingredients.append(ingredient.split(' '))
	allergens.append(allergen.split(', '))
allergens_in_item = dict()
for index, line in enumerate(allergens):
	for product in line:
		if product in allergens_in_item:
			allergens_in_item[product].append(index)
		else:
			lines = list()
			lines.append(index)
			allergens_in_item[product] = lines
ingredient_with_allergen = set()
for key in allergens_in_item:
	list_of_linenb = allergens_in_item[key]
	products_to_check = ingredients[list_of_linenb[0]]
	for item in products_to_check:
		count = 1
		for i in list_of_linenb[1:]:
			if item in ingredients[i]:
				count += 1
		if count == len(list_of_linenb):
			print(item)
			ingredient_with_allergen.add(item)
count = 0
print(ingredient_with_allergen)
for product in ingredients:
	for item in product:
		if item not in ingredient_with_allergen:
			count += 1
print(count)
