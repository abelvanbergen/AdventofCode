data = open("input.txt", "r").read().split("\n")
expenses = [int(i) for i in data];
for i in expenses:
	if 2020 - i in expenses:
		print(i * (2020 - i))
		quit()
