width = 25
length = 6

pixels = open("input.txt").read()[:-1]
step = length * width
rows = [pixels[x*step:(x + 1)*step] for x in range(len(pixels) // step)]
idx = None
for i, row in enumerate(rows):
	new_count = row.count("0")
	print(len(row), new_count)
	if idx == None or new_count < min_count:
		idx = i
		min_count = new_count
print(len(rows))
print(rows[idx].count("1") * rows[idx].count("2"))