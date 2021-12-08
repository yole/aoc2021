def analyze_line(line):
    digits, output = line.split(' | ')
    digits = digits.split()
    output = output.split()
    return len([o for o in output if len(o) in (2, 3, 4, 7)])

result = 0
for line in open("day8input.txt").readlines():
    result += analyze_line(line)
print(result)
