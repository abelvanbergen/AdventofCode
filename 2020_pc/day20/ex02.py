def check_part(up, right, piece):
	for i in range(1, 5):
		if up == piece[i]:
			if (right == piece[i % 4] or):
				return (i)


images = open('input.txt', 'r').read().split('\n\n')
image_data = set()
edge = set()
corner = set()
middle = set()
result = 0
for image in images:
	image = image.replace('\n', '')
	image_id = int(image[5:9])
	image_up = image[10:20]
	image_down = image[100:110]
	image_left = ""
	for i in range(100, 9, -10):
		image_left += image[i]
	image_right = ""
	for i in range(19, 110, 10):
		image_right += image[i]
	print(image_id, image_left)
	quit()
	image_data.add((image_id, image_up, image_right, image_down, image_left, image))
for i in image_data:
	count = 0
	for j in image_data:
		for k in range(1, 5):
			if i[k] in j:
				count += 1
		for k in range(1, 5):
			if i[k][::-1] in j:
				count += 1
	if count == 6:
		corner.add(i)
	elif count == 7:
		edge.add(i)
	else:
		middle.add(i)
Map = set()
elem = corner.pop()
Map.add(elem)
current_pice = elem
for i in range(len(edge)):
	if ()
