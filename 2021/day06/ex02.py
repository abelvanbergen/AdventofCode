def can_reproduce_x_fishes(day_id, fish_age, amount_of_fish):
	total_fish = 1
	d_i = [x for x in range(day_id + fish_age + 1, 18 + 1, 7)]
	for i in d_i:
		total_fish += amount_of_fish[i]
	return(total_fish)

total = 0
amount_of_fish = [0] * 19
fishes = [int(x) for x in open("example.txt").read()[:-1].split(',')]
for i in range(18, -1, -1):
	amount_of_fish[i] = can_reproduce_x_fishes(i, 8, amount_of_fish)
print(amount_of_fish)

for fish in fishes:
	total += amount_of_fish[fish]
print(total)