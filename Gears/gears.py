class GearPair:

    def __init__(self, l_radius, r_radius):
        self.l_radius = l_radius
        self.r_radius = r_radius
        self.left_gear_pairs = []
        self.right_gear_pairs = []

    def set_left_gear_pair(self, gear_pair):
        self.left_gear_pairs.append(gear_pair)

    def set_right_gear_pair(self, gear_pair):
        self.right_gear_pairs.append(gear_pair)


def traverse_path(gear_pair_start, gear_pair_end):
    if len(gear_pair_start.right_gear_pairs) > 0:
        for next_pair in gear_pair_start.right_gear_pairs:
            return traverse_path(next_pair, gear_pair_end)
    else:
        return gear_pair_start == gear_pair_end


def calculate_spacings(peg_list, mult_factor):
    spacing = []
    prev_peg = peg_list[0]
    if prev_peg < 1 or prev_peg > 10000:
        return None
    for peg in peg_list[1:]:
        if peg < 1 or peg > 10000:
            return None
        if peg > prev_peg:
            spacing.append(mult_factor * (peg - prev_peg))
        else:
            return None
        prev_peg = peg
    return spacing


def get_gear_pairs(spacing, mult_factor):
    spacing_pears = []
    for spc in spacing:
        gear_pairs = []
        for l_radius in range(mult_factor, spc):
            r_radius = spc - l_radius
            gear_pairs.append(GearPair(l_radius, r_radius))
        spacing_pears.append(gear_pairs)
    return spacing_pears


def solution(pegs):
    if len(pegs) < 2 or len(pegs) > 20:
        return -1, -1

    mult_factor = 3
    spacing = calculate_spacings(pegs, mult_factor)
    if spacing is None:
        return -1, -1

    spacing_gear_pairs = get_gear_pairs(spacing, mult_factor)

    for idx in range(0, len(spacing_gear_pairs) - 1):
        for gear_pairs in spacing_gear_pairs[idx]:
            r_radius = gear_pairs.r_radius
            for next_radii in spacing_gear_pairs[idx + 1]:
                if next_radii.l_radius == r_radius:
                    next_radii.set_left_gear_pair(gear_pairs)
                    gear_pairs.set_right_gear_pair(next_radii)

    valid_first_last = []
    for first_gear_pair in spacing_gear_pairs[0]:
        for last_gear_pair in spacing_gear_pairs[len(spacing_gear_pairs) - 1]:
            if first_gear_pair.l_radius == last_gear_pair.r_radius * 2:
                valid_first_last.append((first_gear_pair, last_gear_pair))

    for pair in valid_first_last:
        success = traverse_path(pair[0], pair[1])
        if success:
            if pair[0].l_radius % mult_factor == 0:
                return pair[0].l_radius / mult_factor, 1
            else:
                return pair[0].l_radius, mult_factor

    return -1, -1
