from KnightMoves import knight_moves

tests = [
    (1, (19, 36)),
    (3, (0, 1)),
    (0, (1, 1)),
    (1, (0, 10)),
    (0, (-1,0)),
    (0, (0, 64))
]

for test in tests:
    moves = knight_moves.solution(test[1][0], test[1][1])
    if moves == test[0]:
        print('Pass {0}'.format(test[1]))
    else:
        print('Fail {0} - expected {1} got {2}'.format(test[1], test[0], moves))
