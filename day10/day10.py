delimiters = { '(': ')', '[': ']', '{': '}', '<': '>' }
scores = { ')': 3, ']': 57, '}': 1197, '>': 25137 }

def score_line(line):
    stack = []
    for c in line:
        if c in delimiters:
            stack.append(c)
        else:
            opener = stack.pop()
            if delimiters[opener] != c:
                return scores[c]
    return 0

print(sum([score_line(l.strip()) for l in open("day10input.txt").readlines()]))

