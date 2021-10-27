ip_address = open('input.txt').read().splitlines()
answer = 0
for ip in ip_address:
	outer = set()
	inner = set()
	between = 0
	for i in range(len(ip) - 2):
		if ip[i] == '[':
			between = 1
		elif ip[i] == ']':
			between = 0
		elif ip[i] == ip[i + 2] and ip[i] != ip[i + 1]:
			if between == 0:
				outer.add(ip[i:i + 3])
			else:
				inner.add(ip[i + 1] + ip[i:i + 2])
	for com in inner:
		if com in outer:
			print(ip)
			answer += 1
			break
print(answer)