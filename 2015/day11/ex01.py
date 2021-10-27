def get_new_password(password):
	mod_alpha = "abcdefghjkmnpqrstuvwxyza"
	change = 1
	index = 7
	while change == 1:
		change = 0
		index_to_change = mod_alpha.index(password[index]) + 1
		password[index] = mod_alpha[index_to_change]
		if index_to_change == 23:
			change = 1
			index -= 1
	return(''.join(password))

def is_password_valid(password):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	i = 0
	while i < len(password) - 2:
		if password[i:i + 3:] in alphabet:
			break
		i += 1
	if i == len(password) - 2:
		return (0)
	i = 0
	count = 0
	while i < len(password) - 1:
		if (password[i] == password[i + 1]):
			count += 1
			i += 1
		i += 1
	if count < 2:
		return (0)
	return(1)

old_password = open('input_02.txt').read()
new_password = get_new_password(list(old_password))
while is_password_valid(new_password) == 0:
	new_password = get_new_password(list(new_password))
print(new_password)