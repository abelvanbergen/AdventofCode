class Region:
    def __init__(self, x, y, target, depth, erosionLevelUp, erosionLevelLeft):
        self.x = x
        self.y = y
        if ((x, y) in [(0, 0), target]):
            self.geologicIndex = 0
        elif (y == 0):
            self.geologicIndex = x * 16807
        elif (x == 0):
            self.geologicIndex = y * 48271
        else:
            self.geologicIndex = erosionLevelUp * erosionLevelLeft;
        self.erosionLevel = (self.geologicIndex + depth) % 20183
        if (self.erosionLevel % 3 == 0):
            self.type = "rockey"
        elif (self.erosionLevel % 3 == 1):
            self.type = "wet"
        else:
            self.type = "narrow"

    def getRiskLevel(self):
        if (self.type == "rockey"):
            return (0)
        elif (self.type == "wet"):
            return (1)
        else:
            return (2)

    def __str__(self):
        ret = str()
        ret += f"Region x: {self.x} y: {self.y} -=-=-=-\n"
        ret += f"geologicIndex: {self.geologicIndex}\n"
        ret += f"erosionLevel: {self.erosionLevel}\n"
        ret += f"type: {self.type}\n"
        return ret
    
lines = open("input.txt", "r").read().splitlines()
depth = int(lines[0][7:])
targetX, targetY = [int(x) for x in lines[1][8:].split(',')]
caveMap = []
total = 0
for y in range(targetY + 1):
    newLine = []
    for x in range(targetX + 1):
        if x == 0 or y == 0:
            region = Region(x, y, (targetX, targetY), depth, 0, 0)
        else:
            region = Region(x, y, (targetX, targetY), depth, caveMap[y-1][x].erosionLevel, newLine[x-1].erosionLevel)
        newLine.append(region)
        total += region.getRiskLevel()
    caveMap.append(newLine)
print(total)
