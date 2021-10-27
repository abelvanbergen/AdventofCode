ip_address = open('input.txt').read().splitlines()
answer = 0
for ip in ip_address:
	outer = 0
	inner = 0
	between = 0
	for i in range(len(ip) - 3):
		if ip[i] == '[':
			between = 1
		elif ip[i] == ']':
			between = 0
		elif ip[i] == ip[i + 3] and ip[i + 1] == ip[i + 2] and ip[i] != ip[i + 1]:
			if between == 0:
				outer += 1
			else:
				inner += 1
	if outer >= 1 and inner == 0:
		answer += 1
print(answer) 

		
	