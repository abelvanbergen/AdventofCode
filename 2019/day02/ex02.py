from intcode import Intcode

memory_str = open("input.txt").read()
for noun in range(100):
	for ferb in range(100):
		comp = Intcode(memory_str)
		comp.mem_set(1, noun)
		comp.mem_set(2, ferb)
		comp.run()
		if comp.memory[0] == 19690720:
			print("100 * %d + %d = %d" % (noun, ferb, 100*noun + ferb))
			quit()