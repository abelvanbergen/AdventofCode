import statistics
nb = [int(x) for x in open("e").read().split(',')]
print(statistics.median(nb))