from math import sqrt


def calc_gradients(px, py, gx, gy):
    return float(px) / float(py), float(gx) / float(gy)


def cal_top_right_gradients(gloc, ploc, dims):
    p_grad_x = dims[0] - ploc[0]
    p_grad_y = dims[1] - ploc[1]
    g_grad_x = dims[0] - gloc[0]
    g_grad_y = dims[1] - gloc[1]
    p_grad, g_grad = calc_gradients(p_grad_x, p_grad_y, g_grad_x, g_grad_y)
    return g_grad, g_grad_x, p_grad, p_grad_x


def cal_top_left_gradients(gloc, ploc, dims):
    p_grad_x = ploc[0]
    p_grad_y = dims[1] - ploc[1]
    g_grad_x = gloc[0]
    g_grad_y = dims[1] - gloc[1]
    p_grad, g_grad = calc_gradients(p_grad_x, p_grad_y, g_grad_x, g_grad_y)
    return g_grad, g_grad_x, p_grad, p_grad_x


def calc_bottom_left_gradients(gloc, ploc, dims):
    p_grad_x = ploc[0]
    p_grad_y = ploc[1]
    g_grad_x = gloc[0]
    g_grad_y = gloc[1]
    p_grad, g_grad = calc_gradients(p_grad_x, p_grad_y, g_grad_x, g_grad_y)
    return g_grad, g_grad_x, p_grad, p_grad_x


def calc_bottom_right_gradients(gloc, ploc, dims):
    p_grad_x = dims[0] - ploc[0]
    p_grad_y = ploc[1]
    g_grad_x = dims[0] - gloc[0]
    g_grad_y = gloc[1]
    p_grad, g_grad = calc_gradients(p_grad_x, p_grad_y, g_grad_x, g_grad_y)
    return g_grad, g_grad_x, p_grad, p_grad_x


def count_reflect_top_then_bottom(dims, ploc, gloc, max_distance):
    if abs(ploc[0] - gloc[0]) >= 1:
        reflections = 0
        x = (gloc[0] - ploc[0]) ** 2
        for internals in range(0, 1250):
            if internals % 2 == 1:
                y = ((dims[1] - ploc[1]) + (dims[1] * internals) + gloc[1]) ** 2
            else:
                y = ((dims[1] - ploc[1]) + (dims[1] * internals) + (dims[1] - gloc[1])) ** 2
            dist = sqrt(x + y)
            if dist <= max_distance:
                reflections += 1
            else:
                return reflections
    else:
        return 0


def count_reflect_top_then_bottom_with_left(dims, ploc, gloc, max_distance):
    if abs(ploc[0] - gloc[0]) >= 1 and ploc[0] > gloc[0]:
        reflections = 0
        x = (gloc[0] + ploc[0]) ** 2
        for internals in range(1, 1250):
            if internals % 2 == 1:
                y = ((dims[1] - ploc[1]) + (dims[1] * internals) + gloc[1]) ** 2
            else:
                y = ((dims[1] - ploc[1]) + (dims[1] * internals) + (dims[1] - gloc[1])) ** 2
            dist = sqrt(x + y)
            if dist <= max_distance:
                reflections += 1
            else:
                return reflections
    else:
        return 0


def count_reflect_top_then_bottom_with_right(dims, ploc, gloc, max_distance):
    if abs(ploc[0] - gloc[0]) >= 1 and ploc[0] < gloc[0]:
        reflections = 0
        x = (dims[0] - ploc[0] + dims[0] - gloc[0]) ** 2
        for internals in range(1, 1250):
            if internals % 2 == 1:
                y = ((dims[1] - ploc[1]) + (dims[1] * internals) + gloc[1]) ** 2
            else:
                y = ((dims[1] - ploc[1]) + (dims[1] * internals) + (dims[1] - gloc[1])) ** 2
            dist = sqrt(x + y)
            if dist <= max_distance:
                reflections += 1
            else:
                return reflections
    else:
        return 0


def count_reflect_bottom_then_top(dims, ploc, gloc, max_distance):
    if abs(ploc[0] - gloc[0]) >= 1:
        x = (gloc[0] - ploc[0]) ** 2
        reflections = 0
        for internals in range(0, 1250):
            if internals % 2 == 1:
                y = (ploc[1] + (internals * dims[1]) + (dims[1] - gloc[1])) ** 2
            else:
                y = (ploc[1] + (internals * dims[1]) + gloc[1]) ** 2
            dist = sqrt(x + y)
            if dist <= max_distance:
                reflections += 1
            else:
                return reflections
    else:
        return 0


def count_reflect_bottom_then_top_with_left(dims, ploc, gloc, max_distance):
    if abs(ploc[0] - gloc[0]) >= 1 and ploc[0] > gloc[0]:
        x = (gloc[0] + ploc[0]) ** 2
        reflections = 0
        for internals in range(1, 1250):
            if internals % 2 == 1:
                y = (ploc[1] + (internals * dims[1]) + (dims[1] - gloc[1])) ** 2
            else:
                y = (ploc[1] + (internals * dims[1]) + gloc[1]) ** 2
            dist = sqrt(x + y)
            if dist <= max_distance:
                reflections += 1
            else:
                return reflections
    else:
        return 0

def count_reflect_bottom_then_top_with_right(dims, ploc, gloc, max_distance):
    if abs(ploc[0] - gloc[0]) >= 1 and ploc[0] < gloc[0]:
        x = (gloc[0] + ploc[0]) ** 2
        reflections = 0
        for internals in range(1, 1250):
            if internals % 2 == 1:
                y = (ploc[1] + (internals * dims[1]) + (dims[1] - gloc[1])) ** 2
            else:
                y = (ploc[1] + (internals * dims[1]) + gloc[1]) ** 2
            dist = sqrt(x + y)
            if dist <= max_distance:
                reflections += 1
            else:
                return reflections
    else:
        return 0

def count_reflect_left_then_right(dims, ploc, gloc, max_distance):
    if abs(ploc[1] - gloc[1]) >= 1:
        y = (gloc[1] - ploc[1]) ** 2
        reflections = 0
        for internals in range(0, 1250):
            if internals % 2 == 1:
                x = (ploc[0] + (internals * dims[0]) + (dims[0] - gloc[0])) ** 2
            else:
                x = (ploc[0] + (internals * dims[0]) + gloc[0]) ** 2
            dist = sqrt(x + y)
            if dist <= max_distance:
                reflections += 1
            else:
                return reflections
    else:
        return 0


def count_reflect_left_then_right_with_bottom(dims, ploc, gloc, max_distance):
    if abs(ploc[1] - gloc[1]) >= 1 and ploc[1] > gloc[1]:
        y = (ploc[1] + gloc[1]) ** 2
        reflections = 0
        for internals in range(1, 1250):
            if internals % 2 == 1:
                x = (ploc[0] + (internals * dims[0]) + (dims[0] - gloc[0])) ** 2
            else:
                x = (ploc[0] + (internals * dims[0]) + gloc[0]) ** 2
            dist = sqrt(x + y)
            if dist <= max_distance:
                reflections += 1
            else:
                return reflections
    else:
        return 0


def count_reflect_left_then_right_with_top(dims, ploc, gloc, max_distance):
    if abs(ploc[1] - gloc[1]) >= 1 and ploc[1] < gloc[1]:
        y = (dims[1] - ploc[1] + dims[1] - gloc[1]) ** 2
        reflections = 0
        for internals in range(1, 1250):
            if internals % 2 == 1:
                x = (ploc[0] + (internals * dims[0]) + (dims[0] - gloc[0])) ** 2
            else:
                x = (ploc[0] + (internals * dims[0]) + gloc[0]) ** 2
            dist = sqrt(x + y)
            if dist <= max_distance:
                reflections += 1
            else:
                return reflections
    else:
        return 0


def count_reflect_right_then_left(dims, ploc, gloc, max_distance):
    if abs(ploc[1] - gloc[1]) >= 1:
        reflections = 0
        y = (gloc[1] - ploc[1]) ** 2
        for internals in range(0, 1250):
            if internals % 2 == 1:
                x = ((dims[0] - ploc[0]) + (internals * dims[0]) + gloc[0]) ** 2
            else:
                x = ((dims[0] - ploc[0]) + (internals * dims[0]) + (dims[0] - gloc[0])) ** 2
            dist = sqrt(x + y)
            if dist <= max_distance:
                reflections += 1
            else:
                return reflections
    else:
        return 0


def count_reflect_right_then_left_with_top(dims, ploc, gloc, max_distance):
    if abs(ploc[1] - gloc[1]) >= 1 and ploc[1] < gloc[1]:
        reflections = 0
        y = (dims[1] - gloc[1] + dims[1] - ploc[1]) ** 2
        for internals in range(1, 1250):
            if internals % 2 == 1:
                x = ((dims[0] - ploc[0]) + (internals * dims[0]) + gloc[0]) ** 2
            else:
                x = ((dims[0] - ploc[0]) + (internals * dims[0]) + (dims[0] - gloc[0])) ** 2
            dist = sqrt(x + y)
            if dist <= max_distance:
                reflections += 1
            else:
                return reflections
    else:
        return 0


def count_reflect_right_then_left_with_bottom(dims, ploc, gloc, max_distance):
    if abs(ploc[1] - gloc[1]) >= 1 and ploc[1] > gloc[1]:
        reflections = 0
        y = (gloc[1] + ploc[1]) ** 2
        for internals in range(1, 1250):
            if internals % 2 == 1:
                x = ((dims[0] - ploc[0]) + (internals * dims[0]) + gloc[0]) ** 2
            else:
                x = ((dims[0] - ploc[0]) + (internals * dims[0]) + (dims[0] - gloc[0])) ** 2
            dist = sqrt(x + y)
            if dist <= max_distance:
                reflections += 1
            else:
                return reflections
    else:
        return 0


def count_reflect_top(dims, ploc, gloc, max_distance):
    reflections = 0
    for func in [cal_top_left_gradients, cal_top_right_gradients]:
        g_grad, g_grad_x, p_grad, p_grad_x = func(gloc, ploc, dims)
        if g_grad != p_grad:
            x = (p_grad_x + g_grad_x) ** 2
            y = (dims[1] - ploc[1] + dims[1] - gloc[1]) ** 2
            dist = sqrt(x + y)
            if dist <= max_distance:
                reflections += 1
    return reflections


def count_reflect_bottom(dims, ploc, gloc, max_distance):
    reflections = 0
    for func in [calc_bottom_left_gradients, calc_bottom_right_gradients]:
        g_grad, g_grad_x, p_grad, p_grad_x = func(gloc, ploc, dims)
        if g_grad != p_grad:
            x = (p_grad_x + g_grad_x) ** 2
            y = (ploc[1] + gloc[1]) ** 2
            dist = sqrt(x + y)
            if dist <= max_distance:
                reflections += 1
    return reflections


def can_direct(ploc, gloc, max_distance):
    direct = sqrt((ploc[0] - gloc[0]) ** 2 + (ploc[1] - gloc[1]) ** 2)
    return direct <= max_distance


def solution(dims, player_loc, guard_loc, distance):
    hit_count = 0
    if can_direct(player_loc, guard_loc, distance):
        hit_count += 1

    refs = count_reflect_top(dims, player_loc, guard_loc, distance)
    hit_count += refs
    refs = count_reflect_bottom(dims, player_loc, guard_loc, distance)
    hit_count += refs

    refs = count_reflect_top_then_bottom(dims, player_loc, guard_loc, distance)
    hit_count += refs
    refs = count_reflect_bottom_then_top(dims, player_loc, guard_loc, distance)
    hit_count += refs
    refs = count_reflect_right_then_left(dims, player_loc, guard_loc, distance)
    hit_count += refs
    refs = count_reflect_left_then_right(dims, player_loc, guard_loc, distance)
    hit_count += refs

    refs = count_reflect_left_then_right_with_bottom(dims, player_loc, guard_loc, distance)
    hit_count += refs
    refs = count_reflect_right_then_left_with_bottom(dims, player_loc, guard_loc, distance)
    hit_count += refs
    refs = count_reflect_left_then_right_with_top(dims, player_loc, guard_loc, distance)
    hit_count += refs
    refs = count_reflect_right_then_left_with_top(dims, player_loc, guard_loc, distance)
    hit_count += refs

    refs = count_reflect_top_then_bottom_with_left(dims, player_loc, guard_loc, distance)
    hit_count += refs
    refs = count_reflect_top_then_bottom_with_right(dims, player_loc, guard_loc, distance)
    hit_count += refs
    refs = count_reflect_bottom_then_top_with_left(dims, player_loc, guard_loc, distance)
    hit_count += refs
    refs = count_reflect_bottom_then_top_with_right(dims, player_loc, guard_loc, distance)
    hit_count += refs


    return hit_count


if __name__ == '__main__':

    # Test1 = 7
    # Test2 = 9
    # from manual testing <=60
    # Test4 = 0 i.e. no possible result
    # Test5 = 1 i.e. only a direct shot
    # Test6 = 17 [900,700], [853,172], [75,600], 2000
    # Test7 = 12 [200,400], [20,40],[10,2],500
    tests = [
        ([20, 10], [5, 7], [14, 3], 25, 10),
        ([3, 2], [1, 1], [2, 1], 4, 7),
        ([300, 275], [150, 150], [185, 100], 500, 9),
        ([300, 275], [150, 150], [185, 100], 700, 17),
        ([400, 400], [200, 200], [201, 200], 1000, 11),
        ([100, 100], [50, 50], [60, 50], 10, 1),
        ([100, 10], [20, 5], [80, 5], 1000, 399),
        ([900, 700], [853, 172], [75, 600], 2000, 17),
        ([200, 400], [20, 40], [10, 2], 500, 12)
    ]

    for dims, player_loc, guard_loc, distance, shots in tests:
        actual = solution(dims, player_loc, guard_loc, distance)
        if actual == shots:
            print('Pass ({0} {1} {2} {3} -> {4})'.format(dims, player_loc, guard_loc, distance, shots))
        else:
            print('Fail ({0} {1} {2} {3} - expected: {4} actual: {5})'.format(dims, player_loc, guard_loc, distance,
                                                                              shots, actual))
