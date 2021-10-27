def rev_index(string, char):
	return(len(string) - string[::-1].index(char) - 1)

def get_amount_of_distance(lines):
	nbr = 0
	loc = 1
	while nbr != lines:
		nbr += loc
		loc += 1
	return(loc)

def get_char_permute(nbr):
	line = str()
	for i in range(nbr):
		line += str(i)
	return line

def permute(a, l, r):
	global options
	if l==r:
		options.append(a[:])
	else: 
		for i in range(l,r+1): 
			a[l], a[i] = a[i], a[l] 
			permute(a, l+1, r) 
			a[l], a[i] = a[i], a[l]

def get_length_ride(route, relations):
	ret = 0
	for j in range(len(route) - 1):
		if (route[j] < route[j + 1]):
			ret += relations[route[j] + "-" + route[j + 1]]
		else:
			ret += relations[route[j + 1] + "-" + route[j]]
	return ret

distance = open('input.txt').read().splitlines()
amount_of_destinations = get_amount_of_distance(len(distance))
relations = dict()
index = 0
for i in range(amount_of_destinations):
	for j in range(i + 1, amount_of_destinations):
		relations[str(i) + "-" + str(j)] = int(distance[index][rev_index(distance[index], ' ') + 1:])
		index += 1
string = get_char_permute(amount_of_destinations)
a = list(string) 
options = list()
permute(a, 0, amount_of_destinations - 1)
answer = 0
for i in options:
	if get_length_ride(i, relations) > answer:
		answer = get_length_ride(i, relations)
print(answer)