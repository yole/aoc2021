lines = open("day3input.txt").readlines()
values = [int(l, base=2) for l in lines]
mask = 1
gamma = 0
epsilon = 0
for i in range(len(lines[0].strip())):
    ones = len([v for v in values if v & mask])
    if ones > len(values)/2:
        gamma += mask
    else:
        epsilon += mask
    mask *= 2
print(gamma * epsilon)
