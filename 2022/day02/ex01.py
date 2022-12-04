points = [[4,8,3],[1,5,9],[7,2,6]]
lines = open("input.txt").read().splitlines()
print(sum([points[ord(i)-65][ord(k)-88] for i,j,k in lines]))