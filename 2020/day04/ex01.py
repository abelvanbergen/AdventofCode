def is_valid_password(password):
	fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
	count = 0
	for i in fields:
		if i in password:
			count += 1
	return (count == 7)

passports = [i.replace('\n', ' ') for i in open("input.txt", "r").read().split('\n\n')]
print(sum(map(is_valid_password, passports)))
