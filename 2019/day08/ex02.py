width = 25
length = 6

pixels = open("input.txt").read()[:-1].replace("1", "█").replace("0", " ")
step = length * width
layers = [pixels[x*step:(x + 1)*step] for x in range(len(pixels) // step)]
image = ["2"] * len(layers[0])
for layer in layers:
	image = [layer[i] if image[i] == "2" and layer[i] != "2" else image[i] for i in range(len(layer))]
	# for i in range(len(layer)):
	# 	if image[i] == "2" and layer[i] != "2":
	# 		image[i] = layer[i]
image = "".join(image)
for i in range(length):
	print(image[i*width:(i+1)*width])