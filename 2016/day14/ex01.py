from hashlib import md5

def is_key(begin, char):
	to_match = char * 5
	for nb in range(begin, begin + 1000):
		str2hash = key + str(nb)
		res = (md5(str2hash.encode())).hexdigest()
		if to_match in res:
			return (1)
	return (0)

key = "yjdafjpo"
# key = "abc"
num = 0
key_count = 0
while key_count < 64:
	str2hash = key + str(num)
	result = (md5(str2hash.encode())).hexdigest()
	for i in range(len(result) - 2):
		if result[i] == result[i + 1] and result[i] == result[i + 2]:
			if is_key(num + 1, result[i]):
				key_count += 1
			break
	num += 1
print(num - 1)