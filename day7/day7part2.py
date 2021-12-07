positions = [int(x) for x in open("day7input.txt").readline().split(",")]
max_pos = max(positions)
costs = [0] * (max_pos+1)
for crab in positions:
    for x in range(0, max_pos+1):
        dist = abs(crab - x)
        costs[x] += dist * (dist + 1) // 2
print(min(costs))

