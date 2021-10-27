player_1, player_2 = [[int(j) for j in i.split('\n')[1:]] for i in open('input.txt', 'r').read().split('\n\n')]

def make_str_deck(deck):
	string = ""
	for nb in deck:
		string += str(nb)
		string += "-"
	return string

def recursive_combat(deck_1, deck_2):
	mem_player_1 = set()
	mem_player_2 = set()
	while len(deck_1) != 0 and len(deck_2) != 0:
		str_deck_1 = make_str_deck(deck_1)
		str_deck_2 = make_str_deck(deck_2)
		if str_deck_1 in mem_player_1 or str_deck_2 in mem_player_2:
			return (1, deck_1)
		mem_player_1.add(str_deck_1)
		mem_player_2.add(str_deck_2)
		nb_1 = deck_1.pop(0)
		nb_2 = deck_2.pop(0)
		if len(deck_1) >= nb_1 and len(deck_2) >= nb_2:
			winner, winner_nbrs = recursive_combat(deck_1[:nb_1], deck_2[:nb_2])
			if (winner == 1):
				deck_1.append(nb_1)
				deck_1.append(nb_2)
			else:
				deck_2.append(nb_2)
				deck_2.append(nb_1)
		else:
			if (nb_1 > nb_2):
				deck_1.append(nb_1)
				deck_1.append(nb_2)
			else:
				deck_2.append(nb_2)
				deck_2.append(nb_1)
	if len(deck_2) == 0:
		return (1, deck_1)
	else:
		return (2, deck_2)

winner, winner_nbrs = recursive_combat(player_1, player_2)
answer = 0
multi = len(winner_nbrs)
print(winner_nbrs)
for nb in winner_nbrs:
	answer += nb * multi
	multi -= 1
print("winner is player", winner)
print(answer)