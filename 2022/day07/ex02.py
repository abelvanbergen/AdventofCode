def calc_dir_size(dir_name):
	items = files_per_dir[tuple(dir_name)]
	size = 0
	for item in items:
		dir_name.append(item)
		if (tuple(dir_name) in file_sizes.keys()):
			size += file_sizes[tuple(dir_name)]
		else:
			calc_dir_size(dir_name)
			size += dir_sizes[tuple(dir_name)]
		dir_name.pop()
	dir_sizes[tuple(dir_name)] = size

lines = open("input.txt").read().splitlines()
file_sizes = {}
files_per_dir = {}
current_dir = ["/"]
for line in lines[1:]:
	if tuple(current_dir) not in files_per_dir.keys():
		files_per_dir[tuple(current_dir)] = []
	tokens = line.split()
	if (tokens[0] == "$"):
		if (tokens[1] == "ls"):
			continue
		if (tokens[2] == "/"):	
			current_dir = ["/"]
		elif (tokens[2] == ".."):
			current_dir.pop()
		else:
			current_dir.append(tokens[2])
	else:
		if not (tokens[0] == "dir"):
			size = int(tokens[0])
			current_dir.append(tokens[1])
			file_sizes[tuple(current_dir)] = size
			current_dir.pop()
		files_per_dir[tuple(current_dir)].append(tokens[1])
dir_sizes = {}
calc_dir_size(["/"])
needed_space = 30_000_000 - (70000000 - dir_sizes[tuple(["/"])])
smallest = dir_sizes[tuple(["/"])]
for value in dir_sizes.values():
	if value > needed_space and value < smallest:
		smallest = value
print(smallest)
