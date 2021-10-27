def statement1(string):
	for i in range(len(string) - 3):
		needle = string[i:i + 2]
		haystack = string[i + 2:]
		print(needle, haystack)
		if needle in haystack:
			return(1)
	return(0)

def statement2(string):
	for i in range(len(string) - 2):
		if string[i] == string[i + 2]:
			return(1)
	return(0)

def is_nice_string(string):
	return (statement1(string) == 1 and statement2(string) == 1)

strings = open('example.txt').read().splitlines()
answer = 0
for string in strings:
	answer += is_nice_string(string)
print(answer)