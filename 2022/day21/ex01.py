class MathMonkey:
    def __init__(self, name, first, operator, second):
        self.name = name
        self.first = first
        self.second = second
        self.operator = operator

    def __str__(self):
        ret = f"Monkey {self.name} -=-=-=-\n"
        ret += f"first: {self.first}\n"
        ret += f"second: {self.second}\n"
        ret += f"operator: {self.operator}\n"
        return ret

lines = open("input.txt").read().splitlines()
monkey_value = dict()
mathMonkeys = []
for line in lines:
    name, instruction = line.split(": ")
    try:
        nb = int(instruction)
        monkey_value[name] = nb
    except ValueError:
        monkey = MathMonkey(name, *instruction.split())
        mathMonkeys.append(monkey)

while "root" not in monkey_value:
    still_to_check = []
    for monkey in mathMonkeys:
        if monkey.first not in monkey_value:
            still_to_check.append(monkey)
            continue
        if monkey.second not in monkey_value:
            still_to_check.append(monkey)
            continue
        if monkey.operator == "+":
            monkey_value[monkey.name] = monkey_value[monkey.first] + monkey_value[monkey.second]
        elif monkey.operator == "-":
            monkey_value[monkey.name] = monkey_value[monkey.first] - monkey_value[monkey.second]
        elif monkey.operator == "*":
            monkey_value[monkey.name] = monkey_value[monkey.first] * monkey_value[monkey.second]
        else:
            monkey_value[monkey.name] = monkey_value[monkey.first] // monkey_value[monkey.second]
    mathMonkeys = still_to_check
print(monkey_value["root"])

