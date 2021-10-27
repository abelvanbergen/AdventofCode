file = open('input.txt', 'r').read()
string = ""
for char in file:
	string += char + " "
print(string)