print(sum(map(lambda l:(l[2]<=l[0]<=l[3])|(l[0]<=l[2]<=l[1]),[[*map(int,l.replace(*",-").split("-"))]for l in open("i")])))