#get the amount of guests
def get_amount_of_guest(lines):
	nbr = 1
	while nbr * (nbr + 1) != lines:
		nbr += 1
	return(nbr + 1)

#get the index of the x's index in de line
def x_index(amount, char, line):
	count = 0
	i = 0
	while 1:
		if line[i] == char:
			count += 1
		if (count == amount):
			return(i)
		i += 1

#set all possible combinations in a list
#a all char to make a list form
#l which node it is now, start wit 0
#length still to do. len(a) -1 if you want all possible combinations
def permute(a, l, r):
	global options
	if l==r:
		options.append(a[:])
	else: 
		for i in range(l,r+1): 
			a[l], a[i] = a[i], a[l] 
			permute(a, l+1, r) 
			a[l], a[i] = a[i], a[l]

def get_char_permute(nbr):
	line = str()
	for i in range(nbr):
		line += str(i)
	return line

def calc_happiness(combinations, serie):
	ret = 0
	for i in range(len(serie) - 1):
		ret += combinations[str(serie[i]) + "-" + str(serie[i + 1])]
		ret += combinations[str(serie[i + 1]) + "-" + str(serie[i])]
	ret += combinations[str(serie[0]) + "-" + str(serie[len(serie) - 1])]
	ret += combinations[str(serie[len(serie) - 1]) + "-" + str(serie[0])]
	return ret

#parse data
preferences = open('input_02.txt').read().splitlines()
amount_of_guest = get_amount_of_guest(len(preferences))

#get all the data in the right format
#make pairs and add in dict on "guest_1-guest_2" with neg an pos value
combinations = dict()
i = 0
for guest_1 in range(amount_of_guest):
	for guest_2 in range(amount_of_guest):
		if guest_1 != guest_2:
			space_3 = x_index(3, ' ', preferences[i])
			space_4 = x_index(4, ' ', preferences[i])
			nbr = int(preferences[i][space_3 + 1:space_4])
			if "gain" in preferences[i]:
				combinations[str(guest_1) + "-" + str(guest_2)] = nbr
			else:
				combinations[str(guest_1) + "-" + str(guest_2)] = -nbr
			i += 1
options = list()
string = get_char_permute(amount_of_guest)
permute(list(string), 0, amount_of_guest - 1)
answer = 0
for option in options:
	ret = calc_happiness(combinations, option)
	if ret > answer or answer == 0:
		answer = ret
print(answer)
