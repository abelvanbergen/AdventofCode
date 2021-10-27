line = open("input.txt", "r").read().split(" ")
amount_of_players = int(line[0])
last_marble = int(line[6])

score = dict()
for i in range(amount_of_players):
	score[i] = 0

marbles = [0, 1]
index = 1
new_marble = 2
while new_marble <= last_marble:
	if new_marble % 23 == 0:
		score[new_marble % amount_of_players] += new_marble
		index = (index - 7) % len(marbles)
		score[new_marble % amount_of_players] += marbles[index % len(marbles)]
		marbles.remove(marbles[index % len(marbles)])
	else:
		index = (index + 2) % len(marbles)
		marbles.insert(index % len(marbles), new_marble)
	new_marble += 1
	print(new_marble)
highest = 0
for key in score:
	if score[key] > highest:
		highest = score[key]
print(highest)