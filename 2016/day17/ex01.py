from collections import deque
from hashlib import md5

def end(y, x):
	return(x == 3 and y == 3)

def solve(passcode):
	while q:
		key, loc = q.popleft()
		if end(loc[0], loc[1]):
			return(key)
		str2hash = passcode + key
		result = (md5(str2hash.encode())).hexdigest()
		if loc[0] > 0 and result[0] in "bcdef":
			q.append((key + "U", (loc[0] - 1, loc[1])))
		if loc[0] < 3 and result[1] in "bcdef":
			q.append((key + "D", (loc[0] + 1, loc[1])))
		if loc[1] > 0 and result[2] in "bcdef":
			q.append((key + "L", (loc[0], loc[1] - 1)))
		if loc[1] < 3 and result[3] in "bcdef":
			q.append((key + "R", (loc[0], loc[1] + 1)))

passcode = "vwbaicqe"
q = deque()
q.append(("", (0, 0)))
print(solve(passcode))

