import re
inParen = "\(([^()]*)\)"

def calc_nb(line):
	som = line.split(' ')
	result = int(som[0])
	index = 1
	while index < len(som):
		if (som[index] == '*'):
			result *= int(som[index + 1])
		else:
			result += int(som[index + 1])
		index += 2
	return(result)

def calc_line(line):
	while re.search(inParen, line):
		match = re.search(inParen, line)
		nb = calc_nb(match[1])
		line = line[:match.span(0)[0]] + str(nb) + line[match.span(0)[1]:]
	return(calc_nb(line))


data = open('input.txt', 'r').read().splitlines()
answer = 0
for line in data:
	answer += calc_line(line)
print(answer)