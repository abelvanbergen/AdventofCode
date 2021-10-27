def get_element_list(size):
	lst = list()
	for i in range(size):
		lst.append(i)
	return (lst)

element_size = 256
element_list = get_element_list(element_size)
length = [int(x) for x in open('input.txt').read().split(',')]
skip_size = 0
i = 0
for l in length:
	if i + l < len(element_list):
		begin = element_list[:i]
		rev = element_list[i:i + l:]
		rev = rev[::-1]
		end = element_list[i + l:]
		element_list = begin + rev + end
	else:
		# print(len(element_list), end=' ')
		start_len = i + l - len(element_list)
		middle = element_list[start_len:i]
		rev = element_list[i:] + element_list[:start_len]
		rev = rev[::-1]
		start = rev[-start_len:]
		end = rev[:-start_len]
		element_list = start + middle + end
		# print(len(element_list))
	i += l + skip_size
	i = i % element_size
	skip_size += 1
# print(element_list)
print(element_list[0] * element_list[1])

