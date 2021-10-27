passwords = [i.split() for i in open('input.txt').read().splitlines()]
res = 0
for password in passwords:
	count = 0
	for j in range(len(password) - 1):
		for i in range(j + 1, len(password)):
			if password[j] == password[i]:
				count += 1
	if count == 0:
		res += 1
print(res)