from Gears import gears

tests = [
    ((32, 12), [10, 14, 17, 20]),
    ((-1, -1), [10, 11, 12]),
    ((20, 3), [10, 19, 29, 40]),
    ((2, 1), [100, 117, 138, 145]),
    ((10, 1), [24, 46, 63]),
    ((8, 1), [10, 30, 46, 54]),
    ((8, 1), [10, 30, 46]),
    ((12, 1), [4, 30, 50]),
    ((-1, -1), [4, 17, 50]),
    ((-1, -1), [-1, 0]),
    ((-1, -1), [-1, 2]),
    ((-1, -1), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]),
    ((-1, -1), [1, 2, 3, 10001]),
    ((-1, -1), [1]),
    ((-1, -1), [24, 63, 40]),
    ((-1, -1), [24, 24, 40])
]

if __name__ == '__main__':
    for test in tests:
        numerator, denominator = gears.solution(test[1])
        if numerator / denominator == test[0][0] / test[0][1]:
            print('Pass on {0}'.format(test[1]))
        else:
            print('Fail on {0}: expects {1} actual {2}'.format(test[1], test[0], (numerator, denominator)))
