from math import sqrt


def solution(room_space, player_location, guard_location, beam_range):
    hits = 0

    corner_slope_1 =float(room_space[1] - player_location[1]) / float(room_space[0] - player_location[0])
    corner_slope_2 = float(0-player_location[1]) / float(room_space[0] - player_location[0])
    corner_slope_3 = float(room_space[1] - player_location[1]) / float(player_location[0])
    corner_slope_4 = float(-player_location[1]) / float(player_location[0])

    x_range = int(beam_range / room_space[0]) + 1
    y_range = int(beam_range / room_space[1]) + 1
    for y in range(-y_range, y_range):
        for x in range(-x_range, x_range):
            if y % 2 == 0:
                reflected_guard_ypos = room_space[1] * y + guard_location[1]
            else:
                reflected_guard_ypos = room_space[1] * (y + 1) - guard_location[1]

            if x % 2 == 0:
                reflected_guard_xpos = room_space[0] * x + guard_location[0]
            else:
                reflected_guard_xpos = room_space[0] * (x + 1) - guard_location[0]

            xdiff = player_location[0] - reflected_guard_xpos
            ydiff = player_location[1] - reflected_guard_ypos

            if (xdiff != 0 and ydiff != 0) or (x == 0 and y == 0):
                if xdiff != 0 and ydiff != 0:
                    dy = float(ydiff) / float(xdiff)
                if dy not in [corner_slope_1, corner_slope_2, corner_slope_3, corner_slope_4]:
                    hypot = sqrt(xdiff ** 2 + ydiff ** 2)
                    if hypot <= beam_range:
                        hits += 1
    return hits


if __name__ == '__main__':

    # Test1 = 7
    # Test2 = 9
    # from manual testing <=60
    # Test4 = 0 i.e. no possible result
    # Test5 = 1 i.e. only a direct shot
    # Test6 = 17 [900,700], [853,172], [75,600], 2000
    # Test7 = 12 [200,400], [20,40],[10,2],500
    tests = [
        ([3, 2], [1, 1], [2, 1], 4, 7, 'Real Test 1'),
        ([20, 10], [5, 7], [14, 3], 25, 11, ''),
        ([300, 275], [150, 150], [185, 100], 500, 9, 'Real Test 2'),
        ([300, 275], [150, 150], [185, 100], 700, 20, ''),
        ([400, 400], [200, 200], [220, 220], 28, 0, 'Real Test 4'),
        ([100, 100], [50, 50], [60, 50], 10, 1, 'Real Test 5'),
        ([100, 10], [20, 5], [80, 5], 1000, 3151, ''),
        ([900, 700], [853, 172], [75, 600], 2000, 17, 'Real Test 6'),
        ([200, 400], [20, 40], [10, 2], 500, 12, 'Real Test 7')
    ]

    for dims, player_loc, guard_loc, distance, shots, description in tests:
        actual = solution(dims, player_loc, guard_loc, distance)
        if actual == shots:
            print('Pass {5:12} ({0} {1} {2} {3} -> {4})'.format(dims, player_loc, guard_loc, distance, shots,
                                                                description))
        else:
            print('Fail {6:12} ({0} {1} {2} {3} - expected: {4} actual: {5})'.format(dims, player_loc, guard_loc,
                                                                                     distance,
                                                                                     shots, actual, description))
