numbers = sorted([int(i) for i in open("input.txt", "r").read().split('\n')])
memory = [-1 for i in range(len(numbers))]
target = max(numbers)
def recursive_adapter_check(index):
    if memory[index] != -1:
        return memory[index]
    current_num = numbers[index] if index != -1 else 0
    if current_num == target:
        return 1
    total_submatches = 0
    i = 1
    while index + i < len(numbers) and numbers[index + i] - current_num < 4:
        total_submatches += recursive_adapter_check(index + i)
        i += 1
    memory[index] = total_submatches
    return total_submatches
print(recursive_adapter_check(-1))