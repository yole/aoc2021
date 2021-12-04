class Board:
    def __init__(self, f):
        self.lines = []
        for i in range(5):
            l = f.readline().strip()
            self.lines.append([int(n) for n in l.split()])
        self.row_marks = [0] * 5
        self.col_marks = [0] * 5
        self.sum_marked = 0
        self.won = False

    def mark(self, n):
        if self.won: return False 
        for r in range(5):
            for c in range(5):
                if self.lines[r][c] == n:
                    self.row_marks[r] |= (1 << c)
                    self.col_marks[c] |= (1 << r)
                    self.sum_marked += n
                    if self.row_marks[r] == 31 or self.col_marks[c] == 31:
                        self.won = True
                        return True
        return False

    def score(self):
        return sum([sum(r) for r in self.lines]) - self.sum_marked

    def debug_print(self):
        for r in range(5):
            for c in range(5):
                n = self.lines[r][c]
                if self.row_marks[r] & (1 << c):
                    print(f"*{n:2}*", end=' ')
                else:
                    print(f" {n:2} ", end=' ')
            print("")

f = open("day4input.txt")
numbers = [int(n) for n in f.readline().split(",")]
boards = []
while True:
    line = f.readline()
    if not line: break
    boards.append(Board(f))

winners = 0
for n in numbers:
    for b in boards:
        result = b.mark(n)
        if result:
            winners += 1
            if winners == 1 or winners == len(boards):
                print(b.score() * n)

