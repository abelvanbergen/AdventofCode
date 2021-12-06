f=[*map(open("i").read().count,"012345678")]
for _ in[0]*256:f[7]+=f[0];f=f[1:]+f[:1]
print(sum(f))