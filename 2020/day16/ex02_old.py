def is_ticket_valid(ranges, ticket):
	for nb in ticket:
		if not ((nb >= ranges[0] and nb <= ranges[1]) or (nb >= ranges[2] and nb <= ranges[3])):
			return(1)
	return(0)

def is_ticket_valid_for_all_ranges(ranges, ticket):
	count = 0
	for i in ranges:
		count += is_ticket_valid(i, ticket)
	return(count == 20)

restrictions, ticket, data = [i.split('\n') for i in open('input.txt', 'r').read().split('\n\n')]
ranges = []
for i in restrictions:
	lst = i[i.index(':') + 2:]
	lst = [int(j) for j in lst.replace(' or ', '-').split('-')]
	ranges.append(lst)
tickets = []
for i in data[1:]:
	lst = [int(j) for j in i.split(',')]
	tickets.append(lst)
count = 0
for line in tickets:
	if is_ticket_valid_for_all_ranges(ranges, line):
		tickets.remove(line)
		count += 1
colums = [list() for i in range(20)]
for i in range(len(tickets)):
	for j in range(len(colums)):
		colums[j].append(tickets[i][j])
match = [list() for i in range(20)]
for i in range(len(ranges)):
	for j in range(len(colums)):
		if is_ticket_valid(ranges[i], colums[j]) == 0:
			match[i].append(j)
for i in match:
	print(i)