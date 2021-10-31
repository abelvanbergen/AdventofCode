import re

def make_regex_str(all_rules, rule_nb):
	answer = str()
	rule = all_rules[rule_nb].split(' ')
	if rule_nb == 8:
		return "(" + make_regex_str(all_rules, 42) + ")+"
	elif rule_nb == 11:
		answer = "(" + make_regex_str(all_rules, 42) + make_regex_str(all_rules, 31)
		for n in range(2, 7):
			answer += "|" + make_regex_str(all_rules, 42) * n + make_regex_str(all_rules, 31) * n
		answer += ")"
		return(answer)
	elif rule[0][0] == 'a' or rule[0][0] == 'b':
		return(rule[0][0])
	elif "|" in rule:
		answer += "("
		for token in rule:
			if token == "|":
				answer += token
			else:
				answer += make_regex_str(all_rules, int(token))
		answer += ")"
	else:
		for i in rule:
			answer += make_regex_str(all_rules, int(i))
	return(answer)

rules, matches = [i.split('\n') for i in open('input_02.txt').read().replace('\"', '').split('\n\n')]
all_rules = dict()
for line in rules:
	rule_nb, rule = line.split(': ')
	all_rules[int(rule_nb)] = rule
regex_str = "^" + make_regex_str(all_rules, 0) + "$"
answer = 0
for line in matches:
	if (re.search(regex_str, line)):
		answer += 1
print(answer)