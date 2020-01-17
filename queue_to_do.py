def solution(start, length):
    if start < 0 or start > 2000000000 or length < 1 or start + length > 2000000000:
        return 0

    skip_start = length
    checksum = 0
    worker = start
    while skip_start > 0:
        for place in range(0, length):
            if place < skip_start:
                checksum ^= worker
                worker += 1
            else:
                worker += length - place
                break
        skip_start -= 1

    return checksum


def solution2(start, length):
    if start < 0 or start > 2000000000 or length < 1 or start + length > 2000000000:
        return 0

    skip_start = length
    checksum = 0
    worker = start
    while skip_start > 0:
        place = 0
        while place < length:
            if place < skip_start:
                checksum ^= worker
                worker += 1
            else:
                worker += length - place
                break
            place += 1
        skip_start -= 1

    return checksum
