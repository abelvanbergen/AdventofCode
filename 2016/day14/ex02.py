from hashlib import md5

def get_hash(key):
	for i in range(2017):
		key = (md5(key.encode())).hexdigest()
	return(key)

def is_key(begin, char):
	to_match = char * 5
	for nb in range(begin, begin + 1000):
		res = hashes[nb]
		if to_match in res:
			print(nb)
			return (1)
	return (0)

key = "yjdafjpo"
# key = "abc"
num = 0
key_count = 0
hashes = dict()
while key_count < 64:
	if len(hashes) < num + 1010:
		for j in range(5000):
			hashes[num + j] = get_hash(key + str((num + j)))
	result = hashes[num]
	for i in range(len(result) - 2):
		if result[i] == result[i + 1] and result[i] == result[i + 2]:
			if is_key(num + 1, result[i]):
				print(key_count, num)
				key_count += 1
			break
	num += 1
print(num - 1)