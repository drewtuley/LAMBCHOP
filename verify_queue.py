import queue_to_do
import pool_queue

tests = [
    (2, (0, 3)),
    (14, (17, 4)),
    (0, (-1, 0)),
    (82460672, (0, 10000)),
    (0, (2000000001, 10)),
    (0, (2000000000-10, 11))
]

for test in tests:
    start = test[1][0]
    length = test[1][1]
    expected_checksum = test[0]
    checksum = pool_queue.solution(start, length)
    if checksum == expected_checksum:
        print('Pass ({0},{1})'.format(start, length))
    else:
        print('Fail ({0},{1}: expected {2} actual {3})'.format(start, length, expected_checksum, checksum))
