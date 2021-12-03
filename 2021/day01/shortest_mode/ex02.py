d=[int(x)for x in open("i")]
print(sum(map(lambda x,y:x<y,d,d[3:])))