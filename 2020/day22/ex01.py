player_1, player_2 = [[int(j) for j in i.split('\n')[1:]] for i in open('input.txt', 'r').read().split('\n\n')]
while len(player_1) != 0 and len(player_2) != 0:
	nb_1 = player_1.pop(0)
	nb_2 = player_2.pop(0)
	if (nb_1 > nb_2):
		player_1.append(nb_1)
		player_1.append(nb_2)
	else:
		player_2.append(nb_2)
		player_2.append(nb_1)
	print("len player 1:", len(player_1))
if len(player_2) == 0:
	numbers = player_1
else:
	numbers = player_2
multi = len(numbers)
answer = 0
print(numbers)
for nb in numbers:
	answer += nb * multi
	multi -= 1
print(answer)
