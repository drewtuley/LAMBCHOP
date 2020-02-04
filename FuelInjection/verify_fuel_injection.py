from FuelInjection import fuel_injection

if __name__ == "__main__":
    for test in [(2, '3'),
                 (5, '15'),
                 (0, '0'),
                 (0, '1'),
                 (1, '2'),
                 (2, '3'),
                 (2, '4'),
                 (3, '5'),
                 (3, '6'),
                 (4, '7'),
                 (3, '8'),
                 (4, '9'),
                 (4, '10'),
                 (9, '258'),
                 (9, '257'),
                 (17, '65537'),
                 (18, '65539'),
                 (13, '1192'),
                 (238, '1626371727362616172737717726634627273627263726347263726')]:
        expected_steps = test[0]
        pellets = test[1]
        steps = fuel_injection.solution(pellets)
        if steps == expected_steps:
            print('Pass ({0}->{1})'.format(pellets, expected_steps))
        else:
            print('Fail ({0}->{1} - expected: {1}, actual: {2})'.format(pellets, expected_steps, steps))
