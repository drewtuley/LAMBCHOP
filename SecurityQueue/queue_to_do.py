def solution_long(start, length, debug=False):
    """
    Known Working Solution
    :param start:
    :param length:
    :param debug:
    :return:
    """
    if start < 0 or start > 2000000000 or length < 1 or start + length > 2000000000:
        return 0

    skip_start = length
    run_checksum = 0
    worker = start
    while skip_start > 0:
        debug_line = ''
        checksum = 0
        for place in range(0, length):
            if place < skip_start:
                debug_line += '({0}^{1})'.format(checksum, worker)
                checksum ^= worker
                debug_line += '={0} '.format(checksum)
                worker += 1
            else:
                worker += length - place
                break
        skip_start -= 1
        run_checksum ^= checksum
        if debug:
            print(debug_line+' '+str(run_checksum))

    return run_checksum


def solution(start, length):

    if start < 0 or start > 2000000000 or length < 1 or start + length > 2000000000:
        return 0

    check_length = length
    running_checksum = 0
    front_worker = start
    while check_length > 0:
        if check_length > 5:
            repeat_blocks = int(check_length / 4)
            jump_start = (repeat_blocks * 4) + front_worker
            check_from_worker_idx = (repeat_blocks * 4)
            if front_worker % 2 == 0:
                checksum = 0
            else:
                jump_start -= 3
                check_from_worker_idx -= 3
                checksum = front_worker
        else:
            jump_start = front_worker
            checksum = 0
            check_from_worker_idx = 0

        while check_from_worker_idx < check_length:
            checksum ^= jump_start
            jump_start += 1
            check_from_worker_idx += 1

        front_worker += length
        check_length -= 1
        running_checksum ^= checksum
    return running_checksum


if __name__ == "__main__":
    start = 3
    end = 17
    debug = True
    print('<<< old faithful >>>')
    c = solution_long(start, end, debug)
    print('<<< new one >>>')
    c = solution(start, end, debug)
