import threading
import queue


def security_gate(worker, length):
    place = worker
    checksum = 0
    end = worker+length
    while place < end:
        checksum ^= worker
        worker += 1
        place += 1
    return checksum


if __name__ == "__main__":
    start = 17
    length = 4
    run_length = length
    worker = start
    que = queue.Queue()
    acc_checksum = 0
    while run_length > 0:
        w1 = threading.Thread(target=lambda q, a1, a2: q.put(security_gate(a1, a2)), args=(que, worker, run_length))
        w1.start()
        w1.join()
        x = que.get()
        acc_checksum ^= x
        print('start worker {0:5} run_length {1:5} curr_checksum {2:5} acc_checksum {3:5}'.format(worker, run_length, x, acc_checksum))
        worker += length
        run_length -= 1

