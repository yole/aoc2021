def parse_line(l):
    (pair1, pair2) = l.split(" -> ")
    (x1, y1) = pair1.split(",")
    (x2, y2) = pair2.split(",")
    return [int(x1), int(y1), int(x2), int(y2)]

def init_board(max_x, max_y):
    return [[0] * (max_x+1) for i in range(max_y+1)]

def draw_line(line, board, allow_diagonals):
    (x1, y1, x2, y2) = line
    if x1 == x2:
        if y2 < y1: y1, y2 = y2, y1
        for y in range(y1, y2 + 1):
            board[y][x1] += 1
    elif y1 == y2:
        if x2 < x1: x1, x2 = x2, x1
        for x in range(x1, x2 + 1):
            board[y1][x] += 1
    elif allow_diagonals:
        if x2 < x1: x1, y1, x2, y2 = x2, y2, x1, y1
        step_y = 1 if y2 > y1 else -1
        y = y1
        for x in range(x1, x2 + 1):
            board[y][x] += 1
            y += step_y

def print_board(board):
    for line in board:
        print("".join(map(lambda x: str(x) if x else '.', line)))

def count_intersections(board):
    result = 0
    for line in board:
        for cell in line:
            if cell >= 2: result += 1
    return result

def solve_task(allow_diagonals):
    board = init_board(max_x, max_y)
    for line in lines:
        draw_line(line, board, allow_diagonals)

    print_board(board)

    print(count_intersections(board))

lines = [parse_line(l) for l in open("day5input.txt").readlines()]
max_x = max(max([l[0] for l in lines]), max([l[2] for l in lines]))
max_y = max(max([l[1] for l in lines]), max([l[3] for l in lines]))

solve_task(False)
solve_task(True)

