from math import sqrt


def get_quadrant(reflected_guard_xpos, reflected_guard_ypos):
    if reflected_guard_xpos >= 0 and reflected_guard_ypos >= 0:
        return 0
    elif reflected_guard_xpos >= 0 and reflected_guard_ypos < 0:
        return 1
    elif reflected_guard_xpos < 0 and reflected_guard_ypos < 0:
        return 2
    else:
        return 3


def solution(room_space, player_location, guard_location, beam_range):
    hits = 0

    guard_delta_x = player_location[0] - guard_location[0]
    guard_delta_y = player_location[1] - guard_location[1]
    original_guard_slope = None
    if guard_delta_x != 0:
        original_guard_slope = float(guard_delta_y) / float(guard_delta_x)
    original_guard_hypot = sqrt(guard_delta_y ** 2 + guard_delta_x ** 2)

    previous_slope_hits_by_quadrant = [set(), set(), set(), set()]

    x_range = int(beam_range / room_space[0]) + 2
    y_range = int(beam_range / room_space[1]) + 2
    # determine the guard's position in a matrix of reflected rooms around the play space
    # that way, any straight line from player to guard (across the matrix) will be the same as if internally reflected
    # in the play space (that's the theory anyway)
    for y in flip_flop(0, y_range):
        for x in flip_flop(0, x_range):
            if y % 2 == 0:
                reflected_guard_ypos = room_space[1] * y + guard_location[1]
                reflected_player_ypos = room_space[1] * y + player_location[1]
            else:
                reflected_guard_ypos = room_space[1] * (y + 1) - guard_location[1]
                reflected_player_ypos = room_space[1] * (y + 1) - player_location[1]

            if x % 2 == 0:
                reflected_guard_xpos = room_space[0] * x + guard_location[0]
                reflected_player_xpos = room_space[0] * x + player_location[0]
            else:
                reflected_guard_xpos = room_space[0] * (x + 1) - guard_location[0]
                reflected_player_xpos = room_space[0] * (x + 1) - player_location[0]

            reflected_guard_delta_x = player_location[0] - reflected_guard_xpos
            reflected_guard_delta_y = player_location[1] - reflected_guard_ypos

            if (reflected_guard_delta_x != 0 and reflected_guard_delta_y != 0) or (x == 0 and y == 0):
                slope_to_guard = None
                if reflected_guard_delta_x != 0:
                    slope_to_guard = float(reflected_guard_delta_y) / float(reflected_guard_delta_x)
                reflected_player_delta_x = player_location[0] - reflected_player_xpos
                reflected_player_delta_y = player_location[1] - reflected_player_ypos
                slope_to_reflected_player = None
                if reflected_player_delta_x != 0 and reflected_player_delta_y != 0:
                    slope_to_reflected_player = float(reflected_player_delta_y) / float(reflected_player_delta_x)

                player_hypot = sqrt(reflected_player_delta_x ** 2 + reflected_player_delta_y ** 2)
                reflected_guard_hypot = sqrt(reflected_guard_delta_x ** 2 + reflected_guard_delta_y ** 2)
                print('Attempt gx {0:2} gy {1:2} gh {2:3}'.format(reflected_guard_xpos, reflected_guard_ypos,
                                                          reflected_guard_hypot))

                if not (slope_to_guard == original_guard_slope and reflected_guard_hypot > original_guard_hypot):
                    self_hit = False
                    if slope_to_guard is not None and slope_to_reflected_player is not None and slope_to_guard == slope_to_reflected_player and player_hypot < reflected_guard_hypot:
                        self_hit = True
                    quadrant = get_quadrant(reflected_guard_xpos, reflected_guard_ypos)
                    if slope_to_guard not in previous_slope_hits_by_quadrant[quadrant]:
                        if not self_hit and reflected_guard_hypot <= beam_range:
                            print('Accept  gx {0:2} gy {1:2} gh {2:3}'.format(reflected_guard_xpos, reflected_guard_ypos, reflected_guard_hypot))
                            hits += 1
                            previous_slope_hits_by_quadrant[quadrant].add(slope_to_guard)
    return hits


def flip_flop(start, end, step=1):
    delta = step
    while start <= end:
        yield start
        start += (delta * step)
        step += 1
        delta = -delta


if __name__ == '__main__':

    # Test1 = 7
    # Test2 = 9
    # from manual testing <=60
    # Test4 = 0 i.e. no possible result
    # Test5 = 1 i.e. only a direct shot
    # Test6 = 17 [900,700], [853,172], [75,600], 2000
    # Test7 = 12 [200,400], [20,40],[10,2],500
    tests = [
        #([3, 2], [1, 1], [2, 1], 4, 7, 'Real Test 1'),
        # ([4, 3], [3, 2], [2, 1], 5, 5, 'Corners?'),
        # ([20, 10], [5, 7], [14, 3], 25, 11, ''),
        # ([300, 275], [150, 150], [185, 100], 500, 9, 'Real Test 2'),
        # ([300, 275], [150, 150], [185, 100], 700, 20, ''),
        # ([400, 400], [200, 200], [220, 220], 28, 0, 'Real Test 4'),
        # ([100, 100], [50, 50], [60, 50], 10, 1, 'Real Test 5'),
        # ([100, 10], [20, 5], [80, 5], 1000, 2027, ''),
        # ([900, 700], [853, 172], [75, 600], 2000, 17, 'Real Test 6'),
        # ([200, 400], [20, 40], [10, 2], 500, 12, 'Real Test 7'),
        ([2, 5], [1, 2], [1, 4], 11, 27, 'SO2'),  # I get 35 ....
        # ([10, 10], [4, 4], [3, 3], 5000, 739323, 'xx'),
        #([23, 10], [6, 4], [3, 2], 23, 8, 'yy')
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
