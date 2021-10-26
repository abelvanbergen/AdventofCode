IDs = open("input.txt", "r").readlines()
double = 0
triple = 0
for ID in IDs:
	doub, trip = 0, 0
	for letter in "abcdefghijklmnopqrstuvwxyz":
		if (ID.count(letter) == 2 and doub == 0):
			double += 1
			doub += 1
		if (ID.count(letter) == 3 and trip == 0):
			triple += 1
			trip += 1
print(double * triple)
