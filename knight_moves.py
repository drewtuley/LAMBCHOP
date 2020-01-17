from math import sqrt
import operator
import copy

knight_moves = [
    [1, 2], [-1, 2],
    [2, 1], [-2, 1],
    [-1, -2], [1, -2],
    [-2, -1], [2, -1]
]


def get_moves(src, dest):
    x, y = src % 8, int(src / 8)
    dest_x, dest_y = dest % 8, int(dest / 8)
    destinations = []
    for dx, dy in knight_moves:
        if -1 < x + dx < 8 and -1 < y + dy < 8:
            distance = sqrt(abs(x + dx - dest_x) ** 2 + abs(y + dy - dest_y) ** 2)
            destinations.append((distance, (x + dx) + 8 * (y + dy)))
    destinations.sort(key=operator.itemgetter(0))
    return [b for a, b in destinations]


def traverse_map(src, dest, steps, visited, completed_journeys):
    # print(
    #    'src: {0} dest: {1} steps: {2} visited: {3} completed: {4}'.format(src, dest, steps, visited,
    #                                                                      completed_journeys))
    visited.append(src)
    if src == dest:
        completed_journeys.add(steps)
        return True
    else:
        if steps < 7:
            for new_pos in get_moves(src, dest):
                if new_pos not in visited:
                    if new_pos == dest:
                        completed_journeys.add(steps + 1)
                        return True
                    # visited.append(new_pos)
                    v = copy.copy(visited)
                    traverse_map(new_pos, dest, steps + 1, v, completed_journeys)
                    if 1 in completed_journeys:
                        return True
        return False


def solution(src, dest):
    if src == dest:
        return 0
    if -1 < src < 64 and -1 < dest < 64:
        move_list = set()
        traverse_map(src, dest, 0, [], move_list)

        return min(move_list)
    return 0
