def calc_loopsize(value, key, loop):
	while value != door_key:
		value = (value * 7) % 20201227
		loop += 1
	return loop

door_key, card_key = [int(i) for i in open('input.txt', 'r').read().splitlines()]
door_loop_size = calc_loopsize(1, door_key, 0)
value = 1
for i in range(door_loop_size):
	value = (value * card_key) % 20201227
print(value)