lines = open("input.txt").read().splitlines()
part1, part2 = 0, 0
for line in lines:
	start1, end1, start2, end2 = [int(x) for x in line.replace(*",-").split("-")]
	if (start1 >= start2 and end1 <= end2) or (start2 >= start1 and end2 <= end1):
		part1 += 1
	if (start2 <= start1 <= end2) or (start1 <= start2 <= end1):
		part2 += 1
print("part 1:", part1)
print("part 2:", part2)

# for @tbruinem
print(sum(map(lambda l:(l[0]>=l[2])&(l[1]<=l[3])|(l[2]>=l[0])&(l[3]<=l[1]),[[*map(int,l.replace(*",-").split("-"))]for l in open("i")])))
print(sum(map(lambda l:(l[2]<=l[0]<=l[3])|(l[0]<=l[2]<=l[1]),[[*map(int,l.replace(*",-").split("-"))]for l in open("i")])))