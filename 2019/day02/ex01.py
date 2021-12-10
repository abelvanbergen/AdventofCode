from intcode import Intcode

comp = Intcode(open("input.txt").read())
comp.mem_set(1, 12)
comp.mem_set(2, 2)
comp.run()
print(comp.memory[0])