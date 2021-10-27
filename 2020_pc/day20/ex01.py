images = open('input.txt', 'r').read().split('\n\n')
image_data = set()
result = 1
for image in images:
	image = image.replace('\n', '')
	image_id = int(image[5:9])
	image_up = image[10:20]
	image_down = image[100:110]
	image_left = ""
	for i in range(10, 110, 10):
		image_left += image[i]
	image_right = ""
	for i in range(19, 110, 10):
		image_right += image[i]
	image_data.add((image_id, image_up, image_right, image_down, image_left))
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
		result *= i[0]
print(result)