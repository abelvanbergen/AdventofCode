elve_inventory = open("example.txt").read().split('\n\n')
elves = []
for elve in elve_inventory:
	elves.append(sum([int(x) for x in elve.split()]))
print(max(elves))
