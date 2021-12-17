def try_shot(vx, vy, tx0, tx1, ty0, ty1):
    x = 0
    y = 0
    max_y = y
    while True:
        if x > tx1 or y < ty0:
            return None
        if tx0 <= x <= tx1 and ty0 <= y <= ty1:
            return max_y
        x += vx
        y += vy
        if y > max_y: max_y = y
        if vx > 0:
            vx -= 1
        vy -= 1

def find_best_shot(tx0, tx1, ty0, ty1):
    max_y = 0
    count = 0
    for vx in range(0, 1000):
        for vy in range(-1000, 1000):
            my = try_shot(vx, vy, tx0, tx1, ty0, ty1)
            if my is not None: 
                if my > max_y: max_y = my
                count += 1
    return max_y, count

print(find_best_shot(20, 30, -10, -5))
print(find_best_shot(60, 94, -171, -136))

