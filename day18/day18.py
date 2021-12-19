import functools

def parse_number(s):
    result = []
    for c in s:
        match c:
            case '[' | ']':
                result.append(c)
            case ',':
                pass
            case _:
                result.append(int(c))
    return result

def as_str(number):
    s = ""
    nesting = 0
    for n in number:
        if n == '[':
            nesting += 1
            s += "{" if nesting == 5 else '['
        elif n == ']':
            s += '}' if nesting == 5 else ']'
            nesting -= 1
        else:
            s += str(n)
        s += ' '
    return s

def reduce_step(number):
    nesting = 0
    last_seen_number_index = None
    for i, n in enumerate(number):
        if n == '[':
            nesting += 1
        elif n == ']':
            nesting -= 1
        elif nesting == 5:
            if last_seen_number_index is not None:
                number[last_seen_number_index] += n
            for j in range(i+2, len(number)):
                if number[j] != '[' and number[j] != ']':
                    number[j] += number[i+1]
                    break
            number[i-1:i+3] = [0]
            print(f'Explode to {as_str(number)}')
            return True
        else:
            last_seen_number_index = i

    for i, n in enumerate(number):
        if n != '[' and n != ']' and n >= 10:
            number[i:i+1] = ['[', n // 2, n - n // 2, ']']
            print(f'Split to   {as_str(number)}')
            return True
    return False

def add(n1, n2):
    number = ['[']
    number.extend(n1)
    number.extend(n2)
    number.append(']')
    print('Reducing   ' + as_str(number))
    while reduce_step(number): pass
    return number

def magnitude(n, index=0):
    if n[index] == '[':
        index += 1
        m_left, index = magnitude(n, index)
        m_right, index = magnitude(n, index)
        assert n[index] == ']'
        index += 1
        return 3 * m_left + 2 * m_right, index
    return n[index], index+1

numbers = [parse_number(line.strip()) for line in open("day18input.txt")]
result = functools.reduce(add, numbers)
print(magnitude(result)[0])

max_magnitude = 0
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i != j:
            max_magnitude = max(max_magnitude, magnitude(add(numbers[i], numbers[j]))[0])
print(max_magnitude)

