delimiters = { '(': ')', '[': ']', '{': '}', '<': '>' }
scores = { ')': 1, ']': 2, '}': 3, '>': 4 }

def score_line(line):
    stack = []
    for c in line:
        if c in delimiters:
            stack.append(c)
        else:
            opener = stack.pop()
            if delimiters[opener] != c:
                return 0
    result = 0
    while stack:
        opener = stack.pop()
        result = result * 5 + scores[delimiters[opener]]
    return result

scores = [score_line(l.strip()) for l in open("day10input.txt").readlines()]
scores = [s for s in scores if s != 0]
scores.sort()
print(scores[len(scores)//2])

