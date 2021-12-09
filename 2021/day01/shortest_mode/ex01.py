# d=[int(x)for x in open("i")]
d=map(int,open("i"))
print(sum(map(lambda x,y:x<y,d,d[1:])))