grid = [[int(c) for c in line.strip()] for line in open("day11input.txt").readlines()]

def cells():
    for x in range(10):
        for y in range(10):
            yield (x, y)

def neighbors(x, y):
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if 0 <= x + dx < 10 and 0 <= y + dy < 10 and (dx != 0 or dy != 0):
                yield x + dx, y + dy

def step():
    for x, y in cells():
        grid[y][x] += 1

    flashed = set()

    def flash(x, y):
        nonlocal flashed
        if (x, y) in flashed: return
        flashed.add((x, y))
        for nx, ny in neighbors(x, y):
            grid[ny][nx] += 1
            if grid[ny][nx] > 9:
                flash(nx, ny)

    for (x, y) in cells():
        if grid[y][x] > 9:
            flash(x, y)

    for (x, y) in cells():
        if grid[y][x] > 9:
            grid[y][x] = 0

    return len(flashed)

total_flashes = 0
for step_number in range(100):
    total_flashes += step()
    print(f'Step {step_number}: {total_flashes} flashes')

print(total_flashes)

step_number = 100
while True:
    if step() == 100:
        print(step_number + 1)
        break
    step_number += 1
        
