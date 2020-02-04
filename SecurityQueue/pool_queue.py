from multiprocessing import Pool


def security_gate_simple(worker, length):
    place = worker
    checksum = 0
    end = worker + length
    while place < end:
        checksum ^= worker
        worker += 1
        place += 1
    return checksum


def security_gate_striped(worker, length):
    stripe = 15
    place = worker
    checksums = [0 for x in range(0, stripe)]
    gap = int(length / stripe)
    workers = [x * gap for x in range(0, stripe)]
    end = worker + length
    while place < end:
        for x in range(0, stripe):
            checksums[x] ^= workers[x]

        for x in range(0, stripe):
            workers[x] += 1

        place += stripe

    return checksums[0] + checksums[1] + checksums[2] + checksums[3] + checksums[4] + checksums[5] + checksums[6] + \
           checksums[7] + checksums[8] + checksums[9]


def security_gate(worker, length):
    if length < 100:
        return security_gate_simple(worker, length)
    else:
        return security_gate_striped(worker, length)


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
    pool = Pool(processes=4)

    checksum = 0
    for i in pool.imap_unordered(multi_run, starter(start, length)):
        checksum ^= i
    return checksum


def gate_keeper(st, ln):
    rl = ln
    while rl > 0:
        yield st, rl
        st += ln
        rl -= 1


if __name__ == '__main__':
    for s, l in gate_keeper(0, 150):
        chk = security_gate(s, l)
        print('{0},{1}={2} ? {3}'.format(s, l, chk, (s ^ (s + l))))
