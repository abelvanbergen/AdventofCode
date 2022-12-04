class Player:
	def __init__(self, line):
		self.score = 0
		self.pos = int(line.split()[-1])
	
	def move_pawn(self, dice_score):
		self.pos += dice_score
		self.pos = self.pos % 10
		if self.pos == 0:
			self.pos = 10

	def inc_score(self):
		self.score += self.pos

	def has_won(self):
		return self.score >= 1000

class Dice:
	def __init__(self):
		self.loc = 1
		self.stepsize = 3
		self.times_trown = 0
	
	def trow(self):
		dice_score = 0
		for _ in range(self.stepsize):
			dice_score += self.loc
			self.loc += 1
			if (self.loc > 100):
				self.loc = 1
		self.times_trown += 3
		return dice_score

lines = open("input.txt").read().splitlines()
p1 = Player(lines[0])
p2 = Player(lines[1])
dice = Dice()

def take_a_turn(player, dice):
	dice_score = dice.trow()
	player.move_pawn(dice_score)
	player.inc_score()

while True:
	take_a_turn(p1, dice)
	if p1.has_won():
		print(dice.times_trown * p2.score)
		break
	take_a_turn(p2, dice)
	if p2.has_won():
		print(dice.times_trown * p1.score)
		break
