from hashlib import md5

key = "abbhdwsy"
num = 0
answer = ""
while len(answer) < 8:
	str2hash = key + str(num)
	result = (md5(str2hash.encode())).hexdigest()
	if result[:5] == "00000":
		answer += result[5]
	num += 1
print(answer)