def is_gold_bag(bag, content, stri):
	if "shinygold" in stri:
		return (1)
	for i in range(len(bag)):
		if bag[i] in stri:
			new_bags = content[i].split(',')
			for j in new_bags:
				if(is_gold_bag(bag, content, j)):
					return(1)
	return (0)

bags = open("input07.txt", "r").read().replace(' bags', '').replace(' bag', '').replace(' ', '').split('\n')
bag = []
content = []
for i in bags:
	bag_temp, content_temp = i.split('contain')
	bag.append(bag_temp)
	content.append(content_temp)
res = 0
for i in bag:
	if not "shinygold" in i:
		res += is_gold_bag(bag, content, i)
print(res)