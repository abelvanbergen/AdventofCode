print(sum(sorted(sum(map(int,e.split()))for e in open("i").read().split('\n\n'))[-3:]))