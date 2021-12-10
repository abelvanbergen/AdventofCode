d,u,b,a=0,[]," ([{<"," )]}>"
for l in open("i"):
	while(d!=l):
		d=l
		for i in range(5):
			l=l.replace(b[i]+a[i],"")
	if not any(x in l for x in a):
		u.append(sum(5**i*b.index(l[i])for i in range(len(l)-1)))
print(sorted(u)[len(u)//2])