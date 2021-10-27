def count_bag(bag, content, bag_to_check):
	count = 0
	for i in range(len(bag)):					
		if bag[i] in bag_to_check:
			new_bags = content[i].split(',')
			for j in new_bags:
				if "noother" in j:
					return(0)
				count += (int(j[0]) * count_bag(bag, content, j)) + int(j[0])
	return(count)
		
bags = open("inputthijs.txt", "r").read().replace(' ', '').replace('bags', '').replace('bag', '').replace('.', '').split('\n')
bag = []
content = []
for i in bags:
	bag_temp, content_temp = i.split('contain')
	bag.append(bag_temp)
	content.append(content_temp)
print(count_bag(bag, content, "shinygold"))