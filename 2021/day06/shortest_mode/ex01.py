f=[0]*9
for x in open("i").read()[::2]:f[int(x)]+=1
for d in range(256):f[7]+=f[0];f=f[1:]+f[0:1]
print(sum(f))