points = set()
folds = []
file = open("day13input.txt")
reading_folds = False
for line in file.readlines():
    line = line.strip()
    if not line:
        reading_folds = True
        continue
    if reading_folds:
        coord, value = line.split('=')
        folds.append((coord[-1], int(value)))
    else:
        x, y = line.split(',')
        points.add((int(x), int(y)))

def fold(points, coord, value):
    result = set()
    for x, y in points:
        if x > value and coord == 'x':
            result.add((2 * value - x, y))
        elif y > value and coord == 'y':
            folded = (x, 2 * value - y)
            result.add(folded)
        else:
            result.add((x, y))
    return result

def print_grid(points):
    max_x = max([p[0] for p in points])
    max_y = max([p[1] for p in points])
    for y in range(max_y+1):
        print(''.join(['#' if (x, y) in points else ' ' for x in range(max_x+1)]))

coord, value = folds[0]
print(len(fold(points, coord, value)))
for coord, value in folds[1:]:
    points = fold(points, coord, value)
print_grid(points)
