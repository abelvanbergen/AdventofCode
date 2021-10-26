polymer = open("input.txt", "r").read()
alphabet = "abcdefghijklmnopqrstuvwxyz"
cap_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
doubles = []
for i in range(26):
	doubles.append(alphabet[i] + cap_alphabet[i])
	doubles.append(cap_alphabet[i] + alphabet[i])
change = 1
while change == 1:
	change = 0
	for i in range(len(polymer) - 1):
		if polymer[i] + polymer[i + 1] in doubles:
			polymer = polymer.replace(polymer[i] + polymer[i + 1], "")
			# print(polymer)
			change = 1
			break
print(polymer)
print(len(polymer))