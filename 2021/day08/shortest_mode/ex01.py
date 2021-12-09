print(sum(len(e)in[2,3,4,7]for l in open("e") for e in l.split()[11:]))
print(sum(len(e)in[2,3,4,7]for e in open("e").read().split())-800)
print(2000-sum(len(e)in[5,6]for e in open("e").read().split()))
print(2000-sum(4<len(e)<7 for e in open("e").read().split()))