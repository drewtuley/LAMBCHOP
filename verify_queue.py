import queue_to_do

tests = [
    (50, (3948, 11)),
    (56, (18, 7)),
    (2, (0, 3)),
    (14, (17, 4)),
    (0, (-1, 0)),
    (50, (3948, 11)),
    (90, (3948, 12)),
    (6976, (3948, 47)),
    (3085, (3948, 46)),
    (3810, (3948, 45)),
    (6234, (3948, 44)),
    (1745934, (0, 1029)),
    (193728, (304940, 567)),
    (592349, (304940, 566)),
    (0, (2000000001, 333)),
    (0, (2000000000 - 10, 4536))
]

for test in tests:
    start = test[1][0]
    length = test[1][1]
    expected_checksum = test[0]
    checksum = queue_to_do.solution(start, length)
    if checksum == expected_checksum:
        print('Pass ({0},{1})'.format(start, length))
    else:
        print('Fail ({0},{1}): expected {2} actual {3})'.format(start, length, expected_checksum, checksum))
