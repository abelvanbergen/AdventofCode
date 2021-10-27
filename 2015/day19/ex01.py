def is_molecule(line, replacements):
	if line[0] in replacements.keys():
		return(1)
	elif len(line) > 1 and line[:2] in replacements.keys():
		return(2)
	return 0

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
all_options = set()
i = 0
while i < len(molecule):
	len_mol = is_molecule(molecule[i:], replacements)
	if len_mol > 0:
		cur_mol = molecule[i:i + len_mol]
		cur_list = replacements[cur_mol]
		for replacement in cur_list:
			new_str = molecule[:i] + replacement + molecule[i + len_mol:]
			all_options.add(new_str)
		i += len_mol - 1
	i += 1
print(len(all_options))