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
    if ploc[0] != gloc[0]:
        x = (gloc[0] - ploc[0]) ** 2
        y = (gloc[1] + ploc[1]) ** 2
        dist = sqrt(x + y)
        return dist <= max_distance
    else:
        return False


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


def can_reflect_bottom_wall(dims, ploc, gloc, max_distance):
    if ploc[0] != gloc[0]:
        x = (gloc[0] - ploc[0]) ** 2
        y = (dims[1] - gloc[1] + dims[1] - ploc[1]) ** 2
        dist = sqrt(x + y)
        return dist <= max_distance
    else:
        return False


def can_reflect_left_wall(dims, ploc, gloc, max_distance):
    if ploc[1] != gloc[1]:
        x = (gloc[0] + ploc[0]) ** 2
        y = (gloc[1] - ploc[1]) ** 2
        dist = sqrt(x + y)
        return dist <= max_distance
    else:
        return False


def can_reflect_right_wall(dims, ploc, gloc, max_distance):
    if ploc[1] != gloc[1]:
        x = (dims[0] - gloc[0] + dims[0] - ploc[0]) ** 2
        y = (gloc[1] - ploc[1]) ** 2
        dist = sqrt(x + y)
        return dist <= max_distance
    else:
        return False


def solution(dims, player_loc, guard_loc, distance):
    hit_count = 1  # assume a direct shot always
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

    return hit_count


if __name__ == '__main__':
    tests = [
        ([3, 2], [1, 1], [2, 1], 4, 7),
        ([300, 275], [150, 150], [185, 100], 500, 9)
    ]

    for dims, player_loc, guard_loc, distance, shots in tests:
        actual = solution(dims, player_loc, guard_loc, distance)
        if actual == shots:
            print('Pass ({0} {1} {2} {3} -> {4})'.format(dims, player_loc, guard_loc, distance, shots))
        else:
            print('Fail ({0} {1} {2} {3} - expected: {4} actual: {5})'.format(dims, player_loc, guard_loc, distance,
                                                                              shots, actual))
