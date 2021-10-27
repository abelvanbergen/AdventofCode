gen_a, gen_b = [int(i.split()[4])for i in open('input.txt').read().splitlines()]
count = 0
for i in range(5000000):
	gen_a = (gen_a * 16807) % 2147483647
	while gen_a % 4 != 0:
		gen_a = (gen_a * 16807) % 2147483647
	gen_b = (gen_b * 48271) % 2147483647
	while gen_b % 8 != 0:
		gen_b = (gen_b * 48271) % 2147483647
	str_gen_a = format(gen_a, '032b')
	str_gen_b = format(gen_b, '032b')
	if str_gen_a[-16:] == str_gen_b[-16:]:
		count += 1
print(count)