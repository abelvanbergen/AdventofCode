class Tile:
    def __init__(self, max_len):
        self.max_len = max_len
        self.x = 0
        self.y = 0
        self.id = 0
        self.filled = False
        self.grid = [["-"] * max_len for _ in range(max_len)]
        self.point = ""
        self.neighbours = dict()
    
    def set_tile_id(self, tile_id):
        if (self.id == 0):
            self.id = tile_id
            return True
        return False

    def fill_grid(self, char):
        self.grid[self.y][self.x] = char
        self.x += 1
        if (self.x == self.max_len):
            self.x = 0
            self.y += 1
            if (self. y == self.max_len):
                self.filled = True

    def __str__(self):
        ret = f"Tile {self.id} -=-=-\n"
        for line in self.grid:
            ret += "".join(line)
            ret += '\n'
        ret += "neighbours\n"
        for key, value in self.neighbours:
            ret += f"{key}: {value}\n"
        ret += f"point: {self.point}\n"
        return ret
    
    def set_hardcoded_data(self, neighbours, point):
        self.neighbours = neighbours
        self.point = point



grid, instructions_line = open("example.txt").read().split("\n\n")
grid = grid.splitlines()
max_len = 4
tiles = dict()
for j in range(6):
    for i in range(6):
        tiles[(i, j)] = Tile(max_len)
tile_id = 1
for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if char not in "#.":
            continue
        key = (x // max_len, y // max_len)
        tile_set = tiles[key].set_tile_id(tile_id)
        if tile_set:
            tile_id += 1
        tiles[key].fill_grid(char)

new_tiles = dict()
for key, value in tiles.items():
    if value.filled:
        new_tiles[key] = value
tiles = new_tiles
tiles[1].set_hardcoded_data({(1,0):(2, (1,0)),(-1,0):(5, (1,0)),(0,1):(2, (1,0)),(0,-1):(2, (1,0))}, "low")
tiles[2].set_hardcoded_data({}, "low")
tiles[3].set_hardcoded_data()
tiles[4].set_hardcoded_data()
tiles[5].set_hardcoded_data()
tiles[6].set_hardcoded_data()
