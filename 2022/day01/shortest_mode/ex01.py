print(max(sum(map(int,e.split()))for e in open("i").read().split('\n\n')))
print(max(eval(open("i").read().replace(*"\n+").replace("++",",")+"0")))


		