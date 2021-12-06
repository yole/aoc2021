counts_per_age = [0] * 9
counts_per_age[5] = 1
fish_count = []
for day in range(255+5):
    count_zero = counts_per_age[0]
    for i in range(8):
        counts_per_age[i] = counts_per_age[i + 1] 
    counts_per_age[8] = count_zero
    counts_per_age[6] += count_zero
    print(counts_per_age)
    fish_count.append(sum(counts_per_age))
print(fish_count)

input = [int(f) for f in open("day6input.txt").readline().split(",")]
print(sum([fish_count[255+5-f] for f in input]))

