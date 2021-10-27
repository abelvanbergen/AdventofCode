import re
import math

inParen = "\(([^()]*)\)"

def sum_nb(som):
	return(sum([int(i) for i in som.split('+')]))

def calc_nb(line):
	return(math.prod([sum_nb(piece) for piece in line.split('*')]))

def calc_line(line):
	while re.search(inParen, line):
		match = re.search(inParen, line)
		nb = calc_nb(match[1])
		line = line[:match.span(0)[0]] + str(nb) + line[match.span(0)[1]:]
	return(calc_nb(line))

print(sum([calc_line(line) for line in open('input.txt', 'r').read().replace(' ', '').splitlines()]))

# def sum_nb(som):
# 	return(sum([int(i) for i in som.split('+')]))

# def calc_nb(line):
# 	return(math.prod([sum_nb(piece) for piece in line.split('*')]))

# def calc_line(line):
# 	while re.search(inParen, line):
# 		match = re.search(inParen, line)
# 		nb = calc_nb(match[1])
# 		line = line[:match.span(0)[0]] + str(nb) + line[match.span(0)[1]:]
# 	return(calc_nb(line))

# print(sum([calc_line(line) for line in open('input.txt', 'r').read().replace(' ', '').splitlines()]))