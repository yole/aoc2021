position = 0
depth = 0
aim = 0
for line in open("day2input.txt"):
    match line.split():
        case ["forward", n]:
            position += int(n)
            depth += int(n) * aim
        case ["down", n]:
            aim += int(n)
        case ["up", n]:
            aim -= int(n)
print(position * depth)
