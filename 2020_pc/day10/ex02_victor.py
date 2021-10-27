values = sorted([int(i) for i in open("input.txt", "r").read().split("\n")])
jolt = {0:1}
for line in values:
    jolt[line] = 0
    if line - 1 in jolt:
        jolt[line]+=jolt[line-1]
    if line - 2 in jolt:
        jolt[line]+=jolt[line-2]
    if line - 3 in jolt:
        jolt[line]+=jolt[line-3]
print(jolt[max(values)])