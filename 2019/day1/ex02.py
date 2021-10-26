def amount_of_fuel(mass):
	fuel = mass // 3 - 2
	if (fuel > 0):
		return(fuel + amount_of_fuel(fuel))
	else:
		return(0)

mass = [int(i) for i in open("input.txt", "r").read().split('\n')]
print(sum(map(amount_of_fuel, mass)))