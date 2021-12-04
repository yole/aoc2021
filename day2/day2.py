position = 0
depth = 0
for line in open("day2input.txt"):
    match line.split():
        case ["forward", n]:
            position += int(n)
        case ["down", n]:
            depth += int(n)
        case ["up", n]:
            depth -= int(n)
print(position * depth)
