points = [[3,4,8],[1,5,9],[2,6,7]]
lines = open("input.txt").read().splitlines()
print(sum([points[ord(i)-65][ord(k)-88] for i, j, k in lines]))