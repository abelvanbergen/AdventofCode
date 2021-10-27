codes = open('input.txt').read().splitlines()
alphabet = "abcdefghijklmnopqrstuvwxyz"
answer = ""
for i in range(len(codes[0])):
	amount = [1000] * 26
	for j in range(len(codes)):
		amount[alphabet.index(codes[j][i])] = 0
	for j in range(len(codes)):
		amount[alphabet.index(codes[j][i])] += 1
	answer += alphabet[amount.index(min(amount))]
print(answer)