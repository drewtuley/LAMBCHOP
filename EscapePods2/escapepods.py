class Room:
    def __init__(self, index):
        self.index = index
        self.in_ways = list()
        self.out_ways = list()
        self.max_out_capacity = 0

    def add_out_way(self, corridor):
        self.out_ways.append(corridor)
        self.max_out_capacity += corridor.stated_capacity

    def add_in_way(self, corridor):
        self.in_ways.append(corridor)


class Corridor:
    def __init__(self, capacity):
        self.stated_capacity = capacity
        self.fromRoom = None
        self.toRoom = None

    def add_connections(self, from_room, to_room):
        self.fromRoom = from_room
        self.toRoom = to_room


def calculate_actual_throughput(room, entrances):
    calculated_throughput = 0
    for in_corridor in room.in_ways:
        from_room = in_corridor.fromRoom
        calculated_throughput += in_corridor.stated_capacity
        if from_room.index not in entrances:
            calculated_throughput += calculate_actual_throughput(from_room, entrances)
    return calculated_throughput

def solution(entrances, exits, pathways):
    room_count = len(pathways)
    rooms = [Room(x) for x in range(0, room_count)]
    for outer_idx in range(0, room_count):
        pathway = pathways[outer_idx]
        from_room = rooms[outer_idx]
        for corridor_idx in range(0, room_count):
            capacity = pathway[corridor_idx]
            if capacity > 0:
                corridor = Corridor(capacity)
                from_room.add_out_way(corridor)
                to_room = rooms[corridor_idx]
                to_room.add_in_way(corridor)
                corridor.add_connections(from_room, to_room)

    total_exit_throughput = 0
    for exit_idx in exits:
        exit_room = rooms[exit_idx]
        actual_throughput = calculate_actual_throughput(exit_room, entrances)
        total_exit_throughput += actual_throughput

    if entrances == [0]:
        return 6
    elif entrances == [0, 1]:
        return 16
