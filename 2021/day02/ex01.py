instructions = open("i", "r").read().splitlines()
x, y = 0, 0
for instruct in instructions:
	word, nb = instruct.split()
	if word == "forward":
		x += int(nb)
	elif word == "up":
		y -= int(nb)
	else:
		y += int(nb)
print(x * y)

#shortest mode
d={'f':0,'u':0,'d':0}
for x in open("i"):
	c,n=x.split()
	d[c[0]]+=int(n)
print(d['f']*(d['d']-d['u']))

d=[0]*99
for x in open("i"):d[ord(x[0])-99]+=int(x[-2])
print(d[3]*(d[1]-d[18]))