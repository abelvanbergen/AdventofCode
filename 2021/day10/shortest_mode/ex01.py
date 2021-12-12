b=")]}>"
s=[3,57,1197,25137]
t,d=0,0
for l in open("i"):
	while(d!=l):
		d=l
		for c,x in zip("([{<",b):l=l.replace(c+x,"")
	for c in l:
		if c in b:t+=s[b.index(c)];break
print(t)