passwords = [i.split() for i in open('input.txt').read().splitlines()]
res = 0
for password in passwords:
	count = 0
	for j in range(len(password) - 1):
		for i in range(j + 1, len(password)):
			if len(password[j]) == len(password[i]):
				is_not_anagram = 0
				for char in password[j]:
					if char not in password[i]:
						is_not_anagram += 1
				if is_not_anagram == 0:
					count += 1
	if count == 0:
		res += 1
print(res)