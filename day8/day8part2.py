def find_by_length(digits, length):
    return [x for x in digits if len(x) == length]

def decode_digits(digits):
    result = [None] * 10
    result[1] = find_by_length(digits, 2)[0]
    result[7] = find_by_length(digits, 3)[0]
    result[4] = find_by_length(digits, 4)[0]
    maybe_bd = [c for c in result[4] if c not in result[1]]
    six_nine_zero = find_by_length(digits, 6)
    result[0] = [x for x in six_nine_zero if not (maybe_bd[0] in x and maybe_bd[1] in x)][0]
    result[9] = [x for x in six_nine_zero if x != result[0] and result[1][0] in x and result[1][1] in x][0]
    result[6] = [x for x in six_nine_zero if x != result[0] and x != result[9]][0]
    e = [c for c in result[6] if c not in result[9]][0]
    two_three_five = find_by_length(digits, 5)
    result[2] = [x for x in two_three_five if e in x][0]
    result[3] = [x for x in two_three_five if result[1][0] in x and result[1][1] in x][0]
    result[5] = [x for x in two_three_five if x != result[2] and x != result[3]][0]
    result[8] = find_by_length(digits, 7)[0]
    return result

def find_digit(digits, pattern):
    for i in range(10):
        if set(digits[i]) == set(pattern):
            return i

def decode_output(digits, output):
    result = 0
    for o in output:
        result = result * 10 + find_digit(digits, o)
    return result

result = 0
for line in open("day8input.txt").readlines():
    digits, output = line.split(' | ')
    digits = digits.split()
    output = output.split()
    decoded_digits = decode_digits(digits)
    result += decode_output(decoded_digits, output)
print(result)
