def get_len_polymer(polymer):
	change = 1
	while change == 1:
		change = 0
		for i in range(len(polymer) - 1):
			if polymer[i] + polymer[i + 1] in doubles:
				polymer = polymer.replace(polymer[i] + polymer[i + 1], "")
				change = 1
				break
	return(len(polymer))

polymer = open("input.txt", "r").read()
alphabet = "abcdefghijklmnopqrstuvwxyz"
cap_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
doubles = []
for i in range(26):
	doubles.append(alphabet[i] + cap_alphabet[i])
	doubles.append(cap_alphabet[i] + alphabet[i])
shortest = len(polymer)
for i in range(len(alphabet)):
	new_polymer = polymer.replace(alphabet[i], "")
	new_polymer = new_polymer.replace(cap_alphabet[i], "")
	length = get_len_polymer(new_polymer)
	if length < shortest:
		shortest = length
print(shortest)