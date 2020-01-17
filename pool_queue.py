from multiprocessing import Pool, TimeoutError


def security_gate(worker, length):
    place = worker
    checksum = 0
    end = worker + length
    while place < end:
        checksum ^= worker
        worker += 1
        place += 1
    return checksum


def starter(start, length):
    run_length = length
    worker = start
    while run_length > 0:
        yield worker, run_length
        worker += length
        run_length -= 1


def multi_run(args):
    return security_gate(*args)


def solution(start, length):
    if start < 0 or start > 2000000000 or length < 1 or start + length > 2000000000:
        return 0
    pool = Pool(processes=10)

    checksum = 0
    for i in pool.imap_unordered(multi_run, starter(start, length)):
        checksum ^= i
    return checksum


if __name__ == '__main__':
    chk = solution(17, 4)
    print(chk)
