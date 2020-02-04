from BombBaby import bomb_baby

if __name__ == '__main__':
    tests = [
        ('2', '4', 'impossible'),
        ('1123445', '123424', '42'),
        ('1238278', '191829381', '212'),
        ('2', '1', '1'),
        ('4', '7', '4'),
        ('1', '1', '0'),
        ('5', '3', '3'),
        ('12382781', '19182938131', '1596')
    ]

    for m, f, expected in tests:
        actual = bomb_baby.solution(m, f)
        if actual == expected:
            print('Pass ({0},{1})={2}'.format(m, f, expected))
        else:
            print('Fail ({0},{1}) expected: {2} actual: {3}'.format(m, f, expected, actual))
