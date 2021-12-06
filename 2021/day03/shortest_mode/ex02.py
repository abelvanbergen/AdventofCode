def find_csr(bi_nb, char):
	i=0
	while (len(bi_nb)>1):
		new=[]
		test = sum(x[i]>'0'for x in bi_nb)
		test = str(int(2*test//len(bi_nb)==char))
		for nb in bi_nb:
			if nb[i] == test:
				new.append(nb)
		bi_nb=new
		i+=1
	return(bi_nb[0])

bi_nb = open("i", "r").read().splitlines()
#bi_nb = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
csr,ogr=find_csr(bi_nb, 1),find_csr(bi_nb, 0)
print(csr, ogr)
print(int(find_csr(bi_nb, 1),2) * int(find_csr(bi_nb, 0),2))