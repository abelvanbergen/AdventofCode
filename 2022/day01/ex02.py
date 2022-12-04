elve_inventory = open("input.txt").read().split('\n\n')
elves = []
for elve in elve_inventory:
	elves.append(sum([int(x) for x in elve.splitlines()]))
print(sum(sorted(elves)[-3:]))
