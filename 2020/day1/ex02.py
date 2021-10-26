source = open("input01_1", "r");
contents = source.read();
source.close();
expenses = [int(i) for i in contents.split("\n")];
for i in expenses:
	for j in expenses:
		if 2020 - i - j in expenses:
			print (i * j * (2020 - i - j))