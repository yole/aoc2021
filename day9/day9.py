def neighbors(heightmap, x, y):
    if x > 0: yield (x-1, y)
    if x < len(heightmap[y])-1: yield (x+1, y)
    if y > 0: yield (x, y-1)
    if y < len(heightmap)-1: yield (x, y+1)

heightmap_lines = open("day9input.txt").readlines()
heightmap = [[int(c) for c in l.strip()] for l in heightmap_lines]
risk_level = 0
for y in range(len(heightmap)):
    for x in range(len(heightmap[y])):
        lowest_point = True
        for (nx, ny) in neighbors(heightmap, x, y):
            if heightmap[ny][nx] <= heightmap[y][x]:
                lowest_point = False
                break
        if lowest_point:
            risk_level += 1 + heightmap[y][x]

print(risk_level)
