import escapepods

if __name__ == '__main__':
    tests = [
        ([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]], 6),
        ([0, 1], [4, 5],
         [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0]], 16)
    ]
    for entrances, exits, pathways, expected in tests:
        actual = escapepods.solution(entrances, exits, pathways)
        if actual == expected:
            print('Pass')
        else:
            print('Fail')
