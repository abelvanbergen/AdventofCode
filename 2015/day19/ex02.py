def is_molecule(line, replacements):
	if line[0] in replacements.keys():
		return(1)
	elif len(line) > 1 and line[:2] in replacements.keys():
		return(2)
	return 0

def new_molecule(molecule, replacements):
	new_molecule = str()
	for i in replacements:
		cur_list = replacements[i]
		for token in cur_list:
			if token in molecule:
				len_token = len(token)
				new_molecule = molecule[:molecule.index(token)] + i + molecule[molecule.index(token) + len_token:]
				return(new_molecule)

transform, molecule = open('input.txt').read().split('\n\n')
transform = [i.split(' => ') for i in transform.split('\n')]
i = 0
replacements = dict()
while i < len(transform):
	cur_mol = transform[i][0]
	elem_list = list()
	while i < len(transform) and transform[i][0] == cur_mol:
		elem_list.append(transform[i][1])
		i += 1
	replacements[cur_mol] = elem_list

answer = 0
while molecule != "e":
	molecule = new_molecule(molecule, replacements)
	answer += 1
print(answer)
