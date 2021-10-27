def is_hex(nb):
	for char in nb:
		if not char in "0123456789abcdef":
			return 0
	return 1

def is_valid_passport(passport):
	fields = passport.split(' ')
	count = 0
	for i in fields:
		name, value = i.split(':')
		if name == "byr":
			if int(value) >= 1920 and int(value) <= 2002:
				count += 1
		if name == "iyr":
			if int(value) >= 2010 and int(value) <= 2020:
				count += 1
		if name == "eyr":
			if int(value) >= 2020 and int(value) <= 2030:
				count += 1
		if name == "hgt":
			if value[0:-2].isdigit and (value[len(value) - 2:] == "cm" or  value[len(value) - 2:] == "in"):
				nb = int(value[0:-2])
				if value[len(value) - 2:] == "cm" and nb >= 150 and nb <= 193:
					count += 1
				if value[len(value) - 2:] == "in" and nb >= 59 and nb <= 76:
					count += 1
		if name == "hcl":
			if (value[0] == '#' and is_hex(value[1:])):
				count += 1		
		if name == "ecl":
			if value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
				count += 1
		if name == "pid":
			if len(value) == 9 and value.isdigit:
				count += 1
	return(count == 7)

passports = [i.replace('\n', ' ') for i in open("input.txt", "r").read().split('\n\n')]
print(sum(map(is_valid_passport, passports)))