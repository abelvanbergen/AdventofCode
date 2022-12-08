def get_all_dir_form_file(file_name):
	yield("/")
	tokens = file_name.split('/')
	for i in range(2,len(tokens)):
		yield("/".join(tokens[:i]))

def calc_dir_sizes(file_sizes):
	dir_sizes = {}
	for file, size in file_sizes.items():
		for d in get_all_dir_form_file(file):
			if d not in dir_sizes:
				dir_sizes[d] = 0
			dir_sizes[d] += size
	return dir_sizes

def get_name(current_dir, add):
	new = current_dir
	if not len(current_dir) == 1:
		new += "/"
	new += add
	return new

def go_back_one_dir(current_dir):
	new_loc = current_dir[:current_dir.rfind('/')]
	if len(new_loc) == 0:
		new_loc = "/"
	return new_loc

def calc_file_sizes(lines):
	file_sizes = {}
	current_dir = "/"
	for line in lines[1:]:
		tokens = line.split()
		if (tokens[0] == "$"):
			if (tokens[1] == "ls"):
				continue
			if (tokens[2] == "/"):
				current_dir = "/"
			elif (tokens[2] == ".."):
				current_dir = go_back_one_dir(current_dir)
			else:
				current_dir = get_name(current_dir, tokens[2])
		else:
			if not (tokens[0] == "dir"):
				file_name = get_name(current_dir, tokens[1])
				size = int(tokens[0])
				file_sizes[file_name] = size
	return file_sizes

lines = open("input.txt").read().splitlines()
file_sizes = calc_file_sizes(lines)
dir_sizes = calc_dir_sizes(file_sizes)
print("part1:", sum(x for x in dir_sizes.values() if x <= 100000))
needed_space = 30_000_000 - (70_000_000 - dir_sizes["/"])
print("part2:", min(x for x in dir_sizes.values() if x - needed_space >= 0))
