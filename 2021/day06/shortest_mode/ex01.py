f=[*map(open("i").read().count,"012345678")]
# for _ in[0]*256:f[7]+=f[0];f=f[1:]+f[:1]
for i in range(256):f[(i+7)%9]+=f[i%9]
print(sum(f))