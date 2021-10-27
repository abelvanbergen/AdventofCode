def do_fight(cost, boss_hp, player_hp, player_mana, s_c, p_c, r_c):
	boss_damage = 10
	global winner_costs
	if s_c > 0:
		player_armor = 7
		s_c -= 1
	else:
		player_armor = 0
	if p_c > 0:
		boss_hp -= 3
		p_c -= 1
	if r_c > 0:
		player_mana += 101
		r_c -= 1
	if boss_hp <= 0:
		if cost < winner_costs or winner_costs == -1:
			winner_costs = cost
		return
	player_hp = player_hp - 10 + player_armor
	if player_hp <= 0 or (cost > winner_costs and winner_costs != -1):
		return
	if s_c > 0:
		s_c -= 1
	if p_c > 0:
		boss_hp -= 3
		p_c -= 1
	if r_c > 0:
		player_mana += 101
		r_c -= 1
	if boss_hp <= 0:
		if cost < winner_costs or winner_costs == -1:
			winner_costs = cost
		return
	get_all_winners(cost, boss_hp, player_hp, player_mana, s_c, p_c, r_c)
	

def get_all_winners(cost, boss_hp, player_hp, player_mana, s_c, p_c, r_c):
	for i in range(5):
		if i == 0 and player_mana >= 53:
			do_fight(cost + 53, boss_hp - 4, player_hp, player_mana - 53, s_c, p_c, r_c)
		elif i == 1 and player_mana >= 73:
			do_fight(cost + 73, boss_hp - 2, player_hp + 2, player_mana - 73, s_c, p_c, r_c)
		elif i == 2 and player_mana >= 113 and s_c == 0:
			do_fight(cost + 113, boss_hp, player_hp, player_mana - 113, s_c + 6, p_c, r_c)
		elif i == 3 and player_mana >= 173 and p_c == 0:
			do_fight(cost + 173, boss_hp, player_hp, player_mana - 173, s_c, p_c + 6, r_c)
		elif i == 4 and player_mana >= 229 and r_c == 0:
			do_fight(cost + 229, boss_hp, player_hp, player_mana - 229, s_c, p_c, r_c + 5)
	return


boss_hp = 71
player_hp = 50
player_mana = 500
winner_costs = -1
get_all_winners(0, boss_hp, player_hp, player_mana, 0, 0, 0)
print(winner_costs)
