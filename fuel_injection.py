def trailing_zeros(bin_string):
    zeroes = 0
    idx = len(bin_string) - 1
    while idx > 0 and bin_string[idx] == '0':
        idx -= 1
        zeroes += 1
    return zeroes


def shift(value, shifts):
    return value >> shifts


def solution(pellets):
    if len(pellets) > 309:
        return None
    try:
        int_pellets = int(pellets)
        steps = 0
        while int_pellets > 1:
            bin_pellets = '{0:b}'.format(int_pellets)
            bin_pellets_p1 = '{0:b}'.format(int_pellets + 1)
            bin_pellets_m1 = '{0:b}'.format(int_pellets - 1)

            zeroes = trailing_zeros(bin_pellets)
            zeroes_p1 = trailing_zeros(bin_pellets_p1)
            zeroes_m1 = trailing_zeros(bin_pellets_m1)

            z, int_pellets, s = max((zeroes, shift(int_pellets, zeroes), zeroes),
                                    (zeroes_p1, shift(int_pellets + 1, zeroes_p1), zeroes_p1 + 1),
                                    (zeroes_m1, shift(int_pellets - 1, zeroes_m1), zeroes_m1 + 1),
                                    )
            steps += s

        return steps

    except ValueError:
        return None
