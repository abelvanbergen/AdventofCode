def has_won(player_score):
	return player_score >= 21

def get_score(dice_score, player):
	player_pos, player_score = player
	player_pos += dice_score
	player_pos = player_pos % 10
	if player_pos == 0:
		player_pos = 10
	player_score += player_pos
	return (player_pos, player_score)

trows = {3:1, 4:3, 5:6, 6:7, 7:6, 8:3, 9:1}

lines = open("input.txt").read().splitlines()
p1_pos = int(lines[0].split()[-1])
p2_pos = int(lines[1].split()[-1])
p1_wins = 0
p2_wins = 0
def take_turn(p1, p2, step, amount_of_games):
	global p1_wins
	global p2_wins
	if step % 2 == 0:
		if has_won(p2[1]):
			p2_wins += amount_of_games
			return
		for key in trows:
			take_turn(get_score(key, p1), p2, step + 1, amount_of_games * trows[key])
	else:
		if has_won(p1[1]):
			p1_wins += amount_of_games
			return
		for key in trows:
			take_turn(p1, get_score(key, p2), step + 1, amount_of_games * trows[key])

take_turn((p1_pos, 0), (p2_pos, 0), 0, 1)
print(p1_wins if p1_wins > p2_wins else p2_wins)




























def take_turn(p1, p2, step, amount_of_games):
	global p1_wins
	global p2_wins
	if step % 2 == 0:
		if has_won(p2[1]):
			p2_wins += amount_of_games
			return
		for key in trows:
			take_turn(get_score(key, p1), p2, step + 1, amount_of_games * trows[key])
	else:
		if has_won(p1[1]):
			p1_wins += amount_of_games
			return
		for key in trows:
			take_turn(p1, get_score(key, p2), step + 1, amount_of_games * trows[key])


take_turn((p1_pos, 0), (p2_pos, 0), 0, 1)
print(p1_wins if p1_wins > p2_wins else p2_wins)



