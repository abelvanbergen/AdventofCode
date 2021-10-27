def amount_of_fuel(mass):
	return(mass // 3 - 2)

mass = [int(i) for i in open("input.txt", "r").read().split('\n')]
print(sum(map(amount_of_fuel, mass)))

# one liner
#print(sum(map(lambda x: x // 3 - 2, [int(i) for i in open("input.txt", "r").read().split('\n')])))