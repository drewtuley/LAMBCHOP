from math import sqrt, atan2


def solution(room_space, player_location, guard_location, beam_range):
    hits = 0

    x_range = int(beam_range / room_space[0]) + 2
    y_range = int(beam_range / room_space[1]) + 2
    # determine the guard's position in a matrix of reflected rooms around the play space
    # that way, any straight line from player to guard (across the matrix) will be the same as if internally reflected
    # in the play space (that's the theory anyway)
    target_hits = {}
    results = set()
    for i in [0, 1]:
        if i == 0:
            reference = player_location
        else:
            reference = guard_location
        for y in range(-y_range, y_range):
            for x in range(-x_range, x_range):
                if y % 2 == 0:
                    reflected_ypos = room_space[1] * y + reference[1]
                else:
                    reflected_ypos = room_space[1] * (y + 1) - reference[1]

                if x % 2 == 0:
                    reflected_xpos = room_space[0] * x + reference[0]
                else:
                    reflected_xpos = room_space[0] * (x + 1) - reference[0]
                reflected_delta_x = reflected_xpos - player_location[0]
                reflected_delta_y = reflected_ypos - player_location[1]
                beam_theta = atan2(reflected_delta_y, reflected_delta_x)
                beam_length = sqrt(reflected_delta_y ** 2 + reflected_delta_x ** 2)
                if [reflected_xpos, reflected_ypos] != player_location and beam_length <= beam_range:
                    if (beam_theta in target_hits and target_hits[
                        beam_theta] > beam_length) or beam_theta not in target_hits:
                        target_hits[beam_theta] = beam_length
                        if i == 1:
                            results.add(beam_theta)

    return len(results)


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
        ([4, 3], [3, 2], [2, 1], 5, 5, 'Corners?'),
        ([20, 10], [5, 7], [14, 3], 25, 11, ''),
        ([300, 275], [150, 150], [185, 100], 500, 9, 'Real Test 2'),
        ([300, 275], [150, 150], [185, 100], 700, 20, ''),
        ([400, 400], [200, 200], [220, 220], 28, 0, 'Real Test 4'),
        ([100, 100], [50, 50], [60, 50], 10, 1, 'Real Test 5'),
        ([100, 10], [20, 5], [80, 5], 1000, 2571, ''),
        ([900, 700], [853, 172], [75, 600], 2000, 17, 'Real Test 6'),
        ([200, 400], [20, 40], [10, 2], 500, 12, 'Real Test 7'),
        ([2, 5], [1, 2], [1, 4], 11, 27, 'SO2'),
        ([10, 10], [4, 4], [3, 3], 5000, 739323, 'xx'),
        ([23, 10], [6, 4], [3, 2], 23, 8, 'yy')
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
