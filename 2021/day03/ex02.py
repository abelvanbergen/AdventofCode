def count_vertical(array, x, char):
	count = 0
	for j in range(len(array)):
		if array[j][x] == char:
			count += 1
	return (count)

def find_ogr(nbrs):
	i = 0
	while (len(nbrs) != 1 and i < len(nbrs[0])):
		new_list = []
		if (2*count_vertical(nbrs, i, '1')>=len(nbrs)):
			for elem in nbrs:
				if elem[i] != '0':
					new_list.append(elem)
		else:
			for elem in nbrs:
				if elem[i] != '1':
					new_list.append(elem)
		nbrs = new_list
		i+=1
	print(nbrs)
	return ("".join(nbrs[0]))

def find_csr(nbrs):
	i = 0
	while (len(nbrs) != 1 and i < len(nbrs[0])):
		new_list = []
		if (2*count_vertical(nbrs, i, '1')>=len(nbrs)):
			for elem in nbrs:
				if elem[i] != '1':
					new_list.append(elem)
		else:
			for elem in nbrs:
				if elem[i] != '0':
					new_list.append(elem)
		nbrs = new_list
		i+=1
	print(nbrs)
	return ("".join(nbrs[0]))

bi_nb = open("input.txt", "r").read().splitlines()
print(int(find_ogr(bi_nb), 2) * int(find_csr(bi_nb), 2))