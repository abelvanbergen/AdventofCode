total_metadata = 0

def sum_metadata():
    global total_metadata
    global data
    children, metadata = data[:2]
    data = data[2:]
    for c in range(children):
        sum_metadata()
    total_metadata += sum(data[:metadata])
    data = data[metadata:]
    return 

lines = open("input.txt", "r").readlines()
data = [int(x) for x in lines[0].split(' ')]
sum_metadata()
print(total_metadata)