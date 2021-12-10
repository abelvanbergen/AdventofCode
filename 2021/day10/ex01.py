scores = {")":3, "]":57, "}":1197, ">":25137}
combi = {")":"(", "]":"[", "}":"{", ">":"<"}
lines = open("input.txt").read().splitlines()

def get_truncated_line(line):
	old_len = 0
	while (old_len != len(line)):
		old_len = len(line)
		line = line.replace("()", "")
		line = line.replace("<>", "")
		line = line.replace("{}", "")
		line = line.replace("[]", "")
	return (line)

total = 0
for line in lines:
	line = get_truncated_line(line)
	for char in line:
		if (char in scores.keys()):
			total += scores[char]
			break
print(total)