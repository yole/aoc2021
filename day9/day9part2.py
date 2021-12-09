def neighbors(heightmap, x, y):
    if x > 0: yield (x-1, y)
    if x < len(heightmap[y])-1: yield (x+1, y)
    if y > 0: yield (x, y-1)
    if y < len(heightmap)-1: yield (x, y+1)

def basin_size(heightmap, x, y):
    visited = set()
    size = 0
    def flood_fill(x, y):
        nonlocal size
        if not (x, y) in visited and heightmap[y][x] != 9:
            size += 1
            visited.add((x, y))
            for (nx, ny) in neighbors(heightmap, x, y):
                flood_fill(nx, ny)
    flood_fill(x, y)
    return size

heightmap_lines = open("day9input.txt").readlines()
heightmap = [[int(c) for c in l.strip()] for l in heightmap_lines]
lowest_points = []
for y in range(len(heightmap)):
    for x in range(len(heightmap[y])):
        lowest_point = True
        for (nx, ny) in neighbors(heightmap, x, y):
            if heightmap[ny][nx] <= heightmap[y][x]:
                lowest_point = False
                break
        if lowest_point:
            lowest_points.append((x, y))

basins = []
for (x, y) in lowest_points:
    basins.append(basin_size(heightmap, x, y))
basins.sort()
print(basins[-1] * basins[-2] * basins[-3])
