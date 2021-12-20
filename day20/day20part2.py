lines = open("day20input.txt").readlines()
algorithm = lines[0].strip()

def safe_at(grid, x, y, background):
    return background if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[y]) else grid[y][x]

def kernel(grid, x, y, background):
    result = 0
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            pixel = 1 if safe_at(grid, x + dx, y + dy, background) == '#' else 0
            result = result << 1 | pixel
    return result

def enhance_step(grid, background):
    result = []
    for y in range(-1, len(grid)+1):
        line = ''
        for x in range(-1, len(grid[0])+1):
            line += algorithm[kernel(grid, x, y, background)]
        result.append(line)
    print('\n'.join(result) + '\n')
    return result

grid = [line.strip() for line in lines[2:]]
for i in range(50):
    grid = enhance_step(grid, algorithm[0] if i % 2 == 1 else '.')
print(len([c for line in grid for c in line if c != '.']))



