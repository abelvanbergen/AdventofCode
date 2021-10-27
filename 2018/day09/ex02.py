line = open("input.txt", "r").read().split(" ")
amount_of_players = int(line[0])
last_marble = int(line[6]) * 100

marbles = dict()
marbles[0] = [1, 1]
marbles[1] = [0, 0]

score = dict()
for i in range(amount_of_players):
	score[i] = 0

current_marble = 1
new_marble = 2

while new_marble <= last_marble:
	if new_marble % 23 == 0:
		score[new_marble % amount_of_players] += new_marble
		for _ in range (7):
			current_marble = marbles[current_marble][0]
		next_marble = marbles[current_marble][1]
		prev_marble = marbles[current_marble][0]
		marbles[next_marble][0] = prev_marble
		marbles[prev_marble][1] = next_marble
		marbles[current_marble] = "-"
		score[new_marble % amount_of_players] += current_marble
		current_marble = next_marble
	else:
		current_marble = marbles[current_marble][1]
		marbles[new_marble] = [current_marble, marbles[current_marble][1]]
		marbles[marbles[current_marble][1]][0] = new_marble
		marbles[current_marble][1] = new_marble
		current_marble = marbles[current_marble][1]
	new_marble += 1

highest = 0
for key in score:
	if score[key] > highest:
		highest = score[key]
print(highest)