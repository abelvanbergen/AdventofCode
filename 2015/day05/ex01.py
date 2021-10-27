def amount_of_vowels(string):
	ret = 0
	for char in string:
		if char in "aeiou":
			ret+= 1
	return ret
def is_2_char_in_row(string):
	for i in range(len(string) - 1):
		if string[i] == string[i + 1]:
			return(1)
	return(0)

def needles_haystack(needles, haystack):
	for needle in needles:
		if needle in haystack:
			return (1)
	return(0)

def is_nice_string(string):
	if amount_of_vowels(string) < 3:
		return(0)
	if is_2_char_in_row(string) == 0:
		return (0)
	if needles_haystack(["ab", "cd", "pq", "xy"], string) == 1:
		return(0)
	return (1)

strings = open('input.txt').read().splitlines()
answer = 0
for string in strings:
	answer += is_nice_string(string)
print(answer)