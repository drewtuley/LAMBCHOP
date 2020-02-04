def solution(sm, sf):
    m = int(sm)
    f = int(sf)
    if m < f:
        low = m
        hi = f
    else:
        low = f
        hi = m
    generations = 0
    while low > 1 and hi > 1:
        int_gen = int(hi / low)
        generations += int_gen
        new_low = hi - (low * int_gen)
        hi = low
        low = new_low
    if hi < 1 or low < 1:
        return 'impossible'

    generations += hi - low
    return str(generations)
