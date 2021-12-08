lines = open("input.txt", "r").read().splitlines()
count = 0
for line in lines:
	input_value, output_value = line.split(' | ')
	output_value = output_value.split()
	for value in output_value:
		if len(value) in [2, 3, 4, 7]:
			count += 1
print(count)