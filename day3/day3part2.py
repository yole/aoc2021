def choose_by_bit_criterion(values, bits, most_common):
    mask = 1 << (bits-1)
    for i in range(bits):
        for value in values: print(format(value, "012b"))
        ones = len([v for v in values if v & mask])
        one_is_most_common = ones >= len(values)/2
        if one_is_most_common == most_common:
            values = [v for v in values if v & mask]
        else:
            values = [v for v in values if v & mask == 0]
        if len(values) == 1: break
        mask >>= 1
    return values[0]

lines = open("day3input.txt").readlines()
values = [int(l, base=2) for l in lines]
bits = len(lines[0].strip())
oxy_rating = choose_by_bit_criterion(values, bits, True) 
co2_rating = choose_by_bit_criterion(values, bits, False)
print(oxy_rating * co2_rating)
