from GunToGuardFight import gun_to_guard_fight

if __name__ == '__main__':
    tests = [
        ([3, 2], [1, 1], [2, 1], 4, 7),
        ([300, 275], [150, 150], [185, 100], 500, 9)
    ]

    for dims, player_loc, guard_loc, distance, shots in tests:
        actual = gun_to_guard_fight.solution(dims, player_loc, guard_loc, distance)
        if actual == shots:
            print('Pass ({0} {1} {2} {3} -> {4})'.format(dims, player_loc, guard_loc, distance, shots))
        else:
            print('Fail ({0} {1} {2} {3} - expected: {4} actual: {5})'.format(dims, player_loc, guard_loc, distance,
                                                                              shots, actual))
