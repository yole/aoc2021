import collections
import sys

lines = open("day14input.txt").readlines()
template = lines[0].strip()
rules = {}
for line in lines[2:]:
    pair, insertion = line.strip().split(' -> ')
    rules[pair] = insertion

pair_counts = collections.Counter()
for i in range(len(template)-1):
    pair_counts[template[i:i+2]] += 1

for step in range(int(sys.argv[1])):
    result = collections.Counter()
    for pair, count in pair_counts.items():
        insertion = rules.get(pair, None)
        if insertion:
            result[pair[0] + insertion] += count
            result[insertion + pair[1]] += count
        else:
            result[pair] += count
    pair_counts = result

counts = collections.Counter()
for pair, count in pair_counts.items():
    counts[pair[0]] += count
counts[template[-1]] += 1

all_counts = counts.most_common()
print(all_counts[0][1] - all_counts[-1][1])

