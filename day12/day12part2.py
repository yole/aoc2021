import collections

connections = collections.defaultdict(list)
for line in open("day12input.txt").readlines():
    fr, to = line.strip().split('-')
    if to != 'start':
        connections[fr].append(to)
    if fr != 'start':
        connections[to].append(fr)

def generate_paths(point, prev_path, visited_small_cave_twice):
    result = []
    for c in connections[point]:
        if c == 'end':
            result.append(prev_path + ['end'])
        elif c.isupper() or c not in prev_path:
            result.extend(generate_paths(c, prev_path + [c], visited_small_cave_twice))
        elif not visited_small_cave_twice:
            result.extend(generate_paths(c, prev_path + [c], True))
    return result

paths = generate_paths('start', ['start'], False)
print(len(paths))

