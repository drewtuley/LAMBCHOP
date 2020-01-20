import fuel_injection

if __name__ == "__main__":
    for test in [(5, '15'),
                 (2, '4'),
                 (None, 'asdas'),
                 (None, '0'*310),
                 (1, '1'*309)]:
        expected_steps = test[0]
        pellets = test[1]
        steps = fuel_injection.solution(pellets)
        if steps == expected_steps:
            print('Pass ({0}->{1})'.format(pellets, expected_steps))
        else:
            print('Fail ({0}->{1} - expected: {1}, actual: {2})'.format(pellets, expected_steps, steps))
