ips = open('input.txt').read()
alphabet = "abcdefghijklmnopqrstuvwxyz"
for char in alphabet:
	ips = ips.replace(char, '')
ips = ips.splitlines()
for i in ips:
	print(i)