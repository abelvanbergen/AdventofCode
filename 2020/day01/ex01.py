source = open("input01_1", "r");
contents = source.read();
source.close();
expenses = [int(i) for i in contents.split("\n")];
for i in range(len(expenses)):
	for j in expenses[i:]:
		if j + expenses[i] == 2020:
			print(expenses[i] * j);
			quit()
