def solution_long(start, length):
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


def solution(start, length):
    if start < 0 or start > 2000000000 or length < 1 or start + length > 2000000000:
        return 0

    real_length = length
    run_checksum = 0
    worker = start
    while real_length > 0:
        if real_length > 5:
            if worker % 2 == 0:
                blk_len = int(real_length / 4)
                real_start = (blk_len * 4)+worker
                checksum = 0
                steps = (blk_len*4)
            else:
                blk_len = int(real_length / 5)
                real_start = (blk_len * 5)+worker
                checksum = worker
                steps = (blk_len*5)
        else:
            real_start = worker
            checksum = 0
            steps = 0

        while steps < real_length:
            checksum ^= real_start
            real_start += 1
            steps += 1

        worker += length
        real_length -= 1
        run_checksum ^= checksum
    return run_checksum
