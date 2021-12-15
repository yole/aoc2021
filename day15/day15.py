import heapq, collections, sys

grid = [[int(c) for c in line.strip()] for line in open("day15input.txt").readlines()]

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.insert(0, current)
    return total_path

def total_risk(grid, path):
    return sum([grid[y][x] for x, y in path[1:]])

def a_star(grid):
    start = (0, 0)
    max_x = len(grid[0]) - 1
    max_y = len(grid) - 1

    def neighbors(current):
        x, y = current
        if x > 0: yield x-1, y
        if x < max_x: yield x+1, y
        if y > 0: yield x, y-1
        if y < max_y: yield x, y+1

    open_set = [(start, 0)]
    came_from = {}
    g_score = collections.defaultdict(lambda: sys.maxsize)
    g_score[start] = 0

    f_score = collections.defaultdict(lambda: sys.maxsize)
    f_score[start] = 0

    while open_set:
        current = heapq.heappop(open_set)[0]
        if current == (max_x, max_y):
            return reconstruct_path(came_from, current)

        for neighbor in neighbors(current):
            tentative_g_score = g_score[current] + grid[neighbor[1]][neighbor[0]]
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f = tentative_g_score + (max_x - neighbor[0]) + (max_y - neighbor[1])
                heapq.heappush(open_set, (neighbor, f))

print(total_risk(grid, a_star(grid)))

def multiply_line(line, y):
    result = []
    def clip(x): return x - 9 if x > 9 else x
    for x in range(5):
        result.extend([clip(c + x + y) for c in line])
    return result

large_grid = []
for y in range(5):
    for line in grid:
        large_grid.append(multiply_line(line, y))

print(total_risk(large_grid, a_star(large_grid)))

