from re import search


def trailing_binary_zeros(num_pellets):
    bin_string = '{0:b}'.format(num_pellets)
    m = search(r'[1-9][0]+$', bin_string)
    if m is not None:
        return len(m.group(0)) - 1
    else:
        return 0


def solution(pellets):
    int_pellets = int(pellets)
    steps = 0
    while int_pellets > 1:
        if int_pellets == 3:
            steps += 2
            int_pellets = 1
        else:
            shifts, delta = max([(trailing_binary_zeros(int_pellets + delta), delta) for delta in [-1, 0, 1]])
            int_pellets = (int_pellets + delta) >> shifts
            steps += abs(delta) + shifts

    return steps
