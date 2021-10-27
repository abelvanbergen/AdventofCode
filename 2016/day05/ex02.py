from hashlib import md5

def end(lst):
	for item in lst:
		if item == '_':
			return(0)
	return(1)

key = "abbhdwsy"
num = 0
answer = ['_', '_', '_', '_', '_', '_', '_', '_']
while not end(answer):
	str2hash = key + str(num)
	result = (md5(str2hash.encode())).hexdigest()
	if result[:5] == "00000":
		if result[5] >= '0' and result[5] <= '7' and answer[int(result[5])] == '_':
			answer[int(result[5])] = result[6]
			print(''.join(answer))
	num += 1
print(''.join(answer))
