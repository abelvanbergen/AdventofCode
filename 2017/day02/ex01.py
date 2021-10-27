numbers = [[int(x) for x in i.split()] for i in open('input.txt').read().splitlines()]
print(sum(map(lambda x: max(x) - min(x), numbers)))

#one liner
# print(sum(map(lambda x: max(x) - min(x), [[int(x) for x in i.split()] for i in open('input.txt').read().splitlines()])))