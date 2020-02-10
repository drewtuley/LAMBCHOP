from math import sqrt


def calc_gradients(px, py, gx, gy):
    return float(px) / float(py), float(gx) / float(gy)


def cal_top_right_gradients(dims, gloc, ploc):
    p_grad_x = dims[0] - ploc[0]
    p_grad_y = dims[1] - ploc[1]
    g_grad_x = dims[0] - gloc[0]
    g_grad_y = dims[1] - gloc[1]
    p_grad, g_grad = calc_gradients(p_grad_x, p_grad_y, g_grad_x, g_grad_y)
    return g_grad, g_grad_x, p_grad, p_grad_x


def cal_top_left_gradients(dims, gloc, ploc):
    p_grad_x = ploc[0]
    p_grad_y = dims[1] - ploc[1]
    g_grad_x = gloc[0]
    g_grad_y = dims[1] - gloc[1]
    p_grad, g_grad = calc_gradients(p_grad_x, p_grad_y, g_grad_x, g_grad_y)
    return g_grad, g_grad_x, p_grad, p_grad_x


def calc_bottom_left_gradients(gloc, ploc):
    p_grad_x = ploc[0]
    p_grad_y = ploc[1]
    g_grad_x = gloc[0]
    g_grad_y = gloc[1]
    p_grad, g_grad = calc_gradients(p_grad_x, p_grad_y, g_grad_x, g_grad_y)
    return g_grad, g_grad_x, p_grad, p_grad_x


def calc_bottom_right_gradients(dims, gloc, ploc):
    p_grad_x = dims[0] - ploc[0]
    p_grad_y = ploc[1]
    g_grad_x = dims[0] - gloc[0]
    g_grad_y = gloc[1]
    p_grad, g_grad = calc_gradients(p_grad_x, p_grad_y, g_grad_x, g_grad_y)
    return g_grad, g_grad_x, p_grad, p_grad_x


def can_reflect_top_wall(dims, ploc, gloc, max_distance):
    if abs(ploc[0] - gloc[0]) >= 1:
        x = (gloc[0] - ploc[0]) ** 2
        y = (dims[1] - gloc[1] + dims[1] - ploc[1]) ** 2
        dist = sqrt(x + y)
        return dist <= max_distance
    else:
        return False


def can_reflect_top_then_bottom(dims, ploc, gloc, max_distance):
    if abs(ploc[0] - gloc[0]) >= 2:
        reflections = 0
        x = (gloc[0] - ploc[0]) ** 2
        for internals in range(1, 1250):
            y = (gloc[1] + (dims[1] * internals) + dims[1] - ploc[1]) ** 2
            dist = sqrt(x + y)
            if dist <= max_distance:
                reflections += 1
            else:
                return reflections
    else:
        return 0


def can_reflect_bottom_wall(dims, ploc, gloc, max_distance):
    if abs(ploc[0] - gloc[0]) >= 1:
        x = (gloc[0] - ploc[0]) ** 2
        y = (gloc[1] + ploc[1]) ** 2
        dist = sqrt(x + y)
        return dist <= max_distance
    else:
        return False


def can_reflect_bottom_then_top(dims, ploc, gloc, max_distance):
    if abs(ploc[0] - gloc[0]) >= 2:
        x = (gloc[0] - ploc[0]) ** 2
        reflections = 0
        for internals in range(1, 1250):
            y = (dims[1] - gloc[1] + (internals * dims[1]) + ploc[1]) ** 2
            dist = sqrt(x + y)
            if dist <= max_distance:
                reflections += 1
            else:
                return reflections
    else:
        return 0


def can_reflect_left_wall(dims, ploc, gloc, max_distance):
    if abs(ploc[1] - gloc[1]) >= 1:
        x = (gloc[0] + ploc[0]) ** 2
        y = (gloc[1] - ploc[1]) ** 2
        dist = sqrt(x + y)
        return dist <= max_distance
    else:
        return False


def can_reflect_left_then_right(dims, ploc, gloc, max_distance):
    if abs(ploc[1] - gloc[1]) >= 2:
        y = (gloc[1] - ploc[1]) ** 2
        reflections = 0
        for internals in range(1, 1250):
            x = (ploc[0] + (internals * dims[0]) + dims[0] - gloc[0]) ** 2
            dist = sqrt(x + y)
            if dist <= max_distance:
                reflections += 1
            else:
                return reflections
    else:
        return 0


def can_reflect_right_wall(dims, ploc, gloc, max_distance):
    if abs(ploc[1] - gloc[1]) >= 1:
        x = (dims[0] - gloc[0] + dims[0] - ploc[0]) ** 2
        y = (gloc[1] - ploc[1]) ** 2
        dist = sqrt(x + y)
        return dist <= max_distance
    else:
        return False


def can_reflect_right_then_left(dims, ploc, gloc, max_distance):
    if abs(ploc[1] - gloc[1]) >= 2:
        reflections = 0
        y = (gloc[1] - ploc[1]) ** 2
        for internals in range(1, 1250):
            x = (gloc[0] + dims[0] - ploc[0] + (internals * dims[0])) ** 2
            dist = sqrt(x + y)
            if dist <= max_distance:
                reflections += 1
            else:
                return reflections
    else:
        return 0


def can_reflect_top_then_right(dims, ploc, gloc, max_distance):
    g_grad, g_grad_x, p_grad, p_grad_x = cal_top_right_gradients(dims, gloc, ploc)
    if g_grad < p_grad:
        x = (p_grad_x + g_grad_x) ** 2
        y = (dims[1] - ploc[0] + dims[1] - gloc[1]) ** 2
        dist = sqrt(x + y)
        return dist <= max_distance
    else:
        return False


def can_reflect_right_then_top(dims, ploc, gloc, max_distance):
    g_grad, g_grad_x, p_grad, p_grad_x = cal_top_right_gradients(dims, gloc, ploc)
    if g_grad > p_grad:
        x = (p_grad_x + g_grad_x) ** 2
        y = (dims[1] - ploc[0] + dims[1] - gloc[1]) ** 2
        dist = sqrt(x + y)
        return dist <= max_distance
    else:
        return False


def can_reflect_top_then_left(dims, ploc, gloc, max_distance):
    g_grad, g_grad_x, p_grad, p_grad_x = cal_top_left_gradients(dims, gloc, ploc)
    if g_grad < p_grad:
        x = (p_grad_x + g_grad_x) ** 2
        y = (dims[1] - ploc[0] + dims[1] - gloc[1]) ** 2
        dist = sqrt(x + y)
        return dist <= max_distance
    else:
        return False


def can_reflect_left_then_top(dims, ploc, gloc, max_distance):
    g_grad, g_grad_x, p_grad, p_grad_x = cal_top_left_gradients(dims, gloc, ploc)
    if g_grad > p_grad:
        x = (p_grad_x + g_grad_x) ** 2
        y = (dims[1] - ploc[0] + dims[1] - gloc[1]) ** 2
        dist = sqrt(x + y)
        return dist <= max_distance
    else:
        return False


def can_reflect_bottom_then_left(dims, ploc, gloc, max_distance):
    g_grad, g_grad_x, p_grad, p_grad_x = calc_bottom_left_gradients(gloc, ploc)
    if g_grad < p_grad:
        x = (p_grad_x + g_grad_x) ** 2
        y = (ploc[0] + gloc[1]) ** 2
        dist = sqrt(x + y)
        return dist <= max_distance
    else:
        return False


def can_reflect_left_then_bottom(dims, ploc, gloc, max_distance):
    g_grad, g_grad_x, p_grad, p_grad_x = calc_bottom_left_gradients(gloc, ploc)
    if g_grad > p_grad:
        x = (p_grad_x + g_grad_x) ** 2
        y = (ploc[0] + gloc[1]) ** 2
        dist = sqrt(x + y)
        return dist <= max_distance
    else:
        return False


def can_reflect_bottom_then_right(dims, ploc, gloc, max_distance):
    g_grad, g_grad_x, p_grad, p_grad_x = calc_bottom_right_gradients(dims, gloc, ploc)
    if g_grad < p_grad:
        x = (p_grad_x + g_grad_x) ** 2
        y = (ploc[0] + gloc[1]) ** 2
        dist = sqrt(x + y)
        return dist <= max_distance
    else:
        return False


def can_reflect_right_then_bottom(dims, ploc, gloc, max_distance):
    g_grad, g_grad_x, p_grad, p_grad_x = calc_bottom_right_gradients(dims, gloc, ploc)
    if g_grad > p_grad:
        x = (p_grad_x + g_grad_x) ** 2
        y = (ploc[0] + gloc[1]) ** 2
        dist = sqrt(x + y)
        return dist <= max_distance
    else:
        return False


def can_direct(ploc, gloc, max_distance):
    direct = sqrt((ploc[0] - gloc[0]) ** 2 + (ploc[1] - gloc[1]) ** 2)
    return direct <= max_distance


def solution(dims, player_loc, guard_loc, distance):
    hit_count = 0
    if can_direct(player_loc, guard_loc, distance):
        hit_count += 1
    if can_reflect_top_wall(dims, player_loc, guard_loc, distance):
        hit_count += 1
    if can_reflect_bottom_wall(dims, player_loc, guard_loc, distance):
        hit_count += 1
    if can_reflect_left_wall(dims, player_loc, guard_loc, distance):
        hit_count += 1
    if can_reflect_right_wall(dims, player_loc, guard_loc, distance):
        hit_count += 1

    if can_reflect_top_then_right(dims, player_loc, guard_loc, distance):
        hit_count += 1
    if can_reflect_right_then_top(dims, player_loc, guard_loc, distance):
        hit_count += 1
    if can_reflect_top_then_left(dims, player_loc, guard_loc, distance):
        hit_count += 1
    if can_reflect_left_then_top(dims, player_loc, guard_loc, distance):
        hit_count += 1
    if can_reflect_bottom_then_left(dims, player_loc, guard_loc, distance):
        hit_count += 1
    if can_reflect_left_then_bottom(dims, player_loc, guard_loc, distance):
        hit_count += 1
    if can_reflect_bottom_then_right(dims, player_loc, guard_loc, distance):
        hit_count += 1
    if can_reflect_right_then_bottom(dims, player_loc, guard_loc, distance):
        hit_count += 1

    refs = can_reflect_top_then_bottom(dims, player_loc, guard_loc, distance)
    hit_count += refs
    refs = can_reflect_bottom_then_top(dims, player_loc, guard_loc, distance)
    hit_count += refs
    refs = can_reflect_right_then_left(dims, player_loc, guard_loc, distance)
    hit_count += refs
    if can_reflect_left_then_right(dims, player_loc, guard_loc, distance):
        hit_count += 1

    return hit_count


if __name__ == '__main__':

    # Test1 = 7
    # Test2 = 9
    # from manual testing <=50
    # Test4 = 0 i.e. no possible result
    # Test5 = 1 i.e. only a direct shot
    # Test6 = 17 ...
    # Test 6 = 17 [900,700], [853,172], [75,600], 2000

    # Test7 = 12 ...
    tests = [
        ([3, 2], [1, 1], [2, 1], 4, 7),
        ([300, 275], [150, 150], [185, 100], 500, 9),
        ([300, 275], [150, 150], [185, 100], 700, 13),
        ([400, 400], [200, 200], [201, 200], 1000, 7),
        ([100, 100], [50, 50], [60, 50], 10, 1),
        ([100, 10], [20, 5], [80, 5], 1000, 10),
        ([900, 700], [853, 172], [75, 600], 2000, 17)
    ]

    for dims, player_loc, guard_loc, distance, shots in tests:
        actual = solution(dims, player_loc, guard_loc, distance)
        if actual == shots:
            print('Pass ({0} {1} {2} {3} -> {4})'.format(dims, player_loc, guard_loc, distance, shots))
        else:
            print('Fail ({0} {1} {2} {3} - expected: {4} actual: {5})'.format(dims, player_loc, guard_loc, distance,
                                                                              shots, actual))
