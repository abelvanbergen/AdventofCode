s,t,d={")":3,"]":57,"}":1197,">":25137},0,0
for l in open("i"):
	while(d!=l):
		d=l
		for c in["()","[]","{}","<>"]:
			l=l.replace(c,"")
	for c in l:
		if c in")]}>":t+=s[c];break
print(t)