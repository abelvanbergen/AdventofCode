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
	
def fight(player, boss):
	player_damage = player[1] - boss[2]
	if player_damage < 1:
		player_damage = 1
	boss_damage = boss[1] - player[2]
	if boss_damage < 1:
		boss_damage = 1
	while player[0] > 0 and boss[0] > 0:
		boss[0] -= player_damage
		player[0] -= boss_damage
	if boss[0] <= 0:
		return(1)
	return(0)


weapon, armor, ring = [i[i.index('\n') + 1:].split('\n') for i in open('attatchments.txt').read().split('\n\n')]
boss_info = open('input.txt').read().splitlines()
boss = [get_number(1, boss_info[0]), get_number(1, boss_info[1]), get_number(1, boss_info[2])]

weapon_info = dict()
for w in weapon:
	weapon_info[get_number(1, w)] = (get_number(2, w), get_number(3, w))

armor_info = dict()
armor_info[0] = (0, 0)
for a in armor:
	armor_info[get_number(1, a)] = (get_number(2, a), get_number(3, a))

ring_info = dict()
ring_info[0] = (0, 0)
for r in ring:
	ring_info[get_number(2, r)] = (get_number(3, r), get_number(4, r))

lowest = -1
for w in weapon_info:
	for a in armor_info:
		for r_1 in ring_info:
			for r_2 in ring_info:
				if r_1 != r_2:
					cost = w + a + r_1 + r_2
					damage = weapon_info[w][0] + armor_info[a][0] + ring_info[r_1][0] + ring_info[r_2][0]
					armor = weapon_info[w][1] + armor_info[a][1] + ring_info[r_1][1] + ring_info[r_2][1]
					player = [100, damage, armor]
					if fight(player, boss[:]) == 1:
						if (cost < lowest) or lowest == -1:
							lowest = cost
print(lowest)

