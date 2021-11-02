def get_rot_string(line, rot_nb):
	rot = rot_nb % 26
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	new_str = ""
	for char in line:
		if char >= '0' and char <= '9':
			return new_str
		if char == '-':
			new_str += ' '
		else:
			new_str += alphabet[(alphabet.index(char) + rot) % 26]

def get_number(pos, line):
	i = 0
	count = 1
	while 1:
		while line[i] < '0'  or line[i] > '9':
			i += 1
		if count == pos:
			break
		count += 1
		while line[i] >= '0' and line[i] <= '9':
			i += 1
	j = 0
	while i + j != len(line) and (line[i + j] >= '0' and line[i + j] <= '9'):
		j += 1
	return (int(line[i:i + j]))

rooms = open('input.txt').read().splitlines()
answer = 0
all_rooms = dict()
for r in rooms:
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	sector_id = r[-6:-1]
	r = r[:-7]
	room_id = get_number(1, r)
	alphabet_amount = [0] * 26
	for char in alphabet:
		alphabet_amount[alphabet.index(char)] = r.count(char)
	most_commen = ""
	for _ in range(5):
		max_amount = max(alphabet_amount)
		max_char = alphabet[alphabet_amount.index(max_amount)]
		most_commen += max_char
		alphabet.remove(max_char)
		alphabet_amount.remove(max_amount)
	count = 0
	for char in most_commen:
		if char in sector_id:
			count += 1
	if count == 5:
		all_rooms[room_id] = r
for key in all_rooms:
	# if "north" in get_rot_string(all_rooms[key], key):
	print(key, get_rot_string(all_rooms[key], key))
