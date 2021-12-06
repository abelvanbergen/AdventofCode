amount_of_days = 256

def can_reproduce_x_fishes(day_of_birth, amount_of_fish):
	total_fish = 1
	d_i = [x for x in range(day_of_birth + 9, amount_of_days + 1, 7)]
	print(d_i)
	for i in d_i:
		total_fish += amount_of_fish[i]
	return(total_fish)

fishes = [int(x) for x in open("input.txt").read()[:-1].split(',')]
total = 0
amount_of_fish = [0] * (amount_of_days + 1)
for i in range(amount_of_days, -1, -1):
	amount_of_fish[i] = can_reproduce_x_fishes(i, amount_of_fish)
for fish in fishes:
	childs = d_i = [x for x in range(fish + 1, amount_of_days + 1, 7)]
	for child in childs:
		total += amount_of_fish[child]
	total += 1
print(total)