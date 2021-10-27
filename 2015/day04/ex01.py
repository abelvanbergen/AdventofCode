from hashlib import md5

key = "iwrupvqb"
num = 0
while 1:
	str2hash = key + str(num)
	result = (md5(str2hash.encode())).hexdigest()
	if result[:5] == "00000":
		print(num)
		quit()
	num += 1