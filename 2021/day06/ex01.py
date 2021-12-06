fishes = [int(x) for x in open("input.txt").read()[:-1].split(',')]
for j in range(256):
	new_born = []
	for i, fish in enumerate(fishes):
		if fish == 0:
			new_born.append(8)
			fishes[i] = 7
		fishes[i] -= 1
	fishes += new_born
	print(j)
	# print(fishes)
print(len(fishes))