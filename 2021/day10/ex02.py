scores = {")":3, "]":57, "}":1197, ">":25137}
non_corrupted_score = {"(":1, "[":2, "{":3, "<":4}
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
all_scores = []
for line in lines:
	line = get_truncated_line(line)
	corrupted = 0
	for char in line:
		if (char in scores.keys()):
			corrupted = 1
	if (corrupted == 0):
		score = 0
		for char in line[::-1]:
			score *= 5
			score += non_corrupted_score[char]
		all_scores.append(score)
print(all_scores)
all_scores.sort()
print(len(all_scores))
print(all_scores[len(all_scores)//2])