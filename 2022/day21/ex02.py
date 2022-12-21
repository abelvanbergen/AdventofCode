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
mathMonkeys = dict()
for line in lines:
    name, instruction = line.split(": ")
    try:
        nb = int(instruction)
        if name == "humn":
            continue
        monkey_value[name] = nb
    except ValueError:
        monkey = MathMonkey(name, *instruction.split())
        mathMonkeys[name] = monkey

root_first, root_second = mathMonkeys["root"].first, mathMonkeys["root"].second
change = True
while change:
    change = False
    still_to_check = dict()
    for monkey in mathMonkeys.values():
        if monkey.first not in monkey_value:
            still_to_check[monkey.name] = monkey
            continue
        if monkey.second not in monkey_value:
            still_to_check[monkey.name] = monkey
            continue
        change = True
        if monkey.operator == "+":
            monkey_value[monkey.name] = monkey_value[monkey.first] + monkey_value[monkey.second]
        elif monkey.operator == "-":
            monkey_value[monkey.name] = monkey_value[monkey.first] - monkey_value[monkey.second]
        elif monkey.operator == "*":
            monkey_value[monkey.name] = monkey_value[monkey.first] * monkey_value[monkey.second]
        else:
            monkey_value[monkey.name] = monkey_value[monkey.first] // monkey_value[monkey.second]
    mathMonkeys = still_to_check

if root_first in monkey_value:
    monkey_value[root_second] = monkey_value[root_first]
    new = root_second
else:
    monkey_value[root_first] = monkey_value[root_second]
    new = root_first



while new != "humn":
    monkey = mathMonkeys[new]
    if monkey.operator == "+":
        if monkey.first in monkey_value:
            monkey_value[monkey.second] = monkey_value[monkey.name] - monkey_value[monkey.first]
            new = monkey.second
        else:
            monkey_value[monkey.first] = monkey_value[monkey.name] - monkey_value[monkey.second]
            new = monkey.first
    elif monkey.operator == "-":
        if monkey.first in monkey_value:
            monkey_value[monkey.second] = monkey_value[monkey.first] - monkey_value[monkey.name]
            new = monkey.second
        else:
            monkey_value[monkey.first] = monkey_value[monkey.name] + monkey_value[monkey.second]
            new = monkey.first
    elif monkey.operator == "*":
        if monkey.first in monkey_value:
            monkey_value[monkey.second] = monkey_value[monkey.name] // monkey_value[monkey.first]
            new = monkey.second
        else:
            monkey_value[monkey.first] = monkey_value[monkey.name] // monkey_value[monkey.second]
            new = monkey.first
    else:
        if monkey.first in monkey_value:
            monkey_value[monkey.second] = monkey_value[monkey.first] // monkey_value[monkey.first]
            new = monkey.second
        else:
            monkey_value[monkey.first] = monkey_value[monkey.name] * monkey_value[monkey.second]
            new = monkey.first
print(monkey_value["humn"])
