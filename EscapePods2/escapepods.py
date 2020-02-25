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

    def get_total_input(self):
        return reduce(lambda x, y: x + y, [inway.stated_capacity for inway in self.in_ways])

    def get_total_output(self):
        return reduce(lambda x, y: x + y, [outway.stated_capacity for outway in self.out_ways])

    def get_fattest_input_corridor(self):
        return max(self.in_ways, key=lambda i: i.stated_capacity)

    def get_fattest_output_corridor(self):
        return max(self.out_ways, key=lambda i: i.stated_capacity)


class Corridor:
    def __init__(self, capacity):
        self.stated_capacity = capacity
        self.from_room = None
        self.to_room = None

    def add_connections(self, from_room, to_room):
        self.from_room = from_room
        self.to_room = to_room


def calculate_actual_throughput(room, entrances, exits):
    theoretical_input = room.get_total_input()

    if theoretical_input < room.max_out_capacity:
        # reduce the output corridors capacity to match the room's actual input capacity
        if room.index not in exits:
            while theoretical_input < room.max_out_capacity:
                fattest_corridor = room.get_fattest_output_corridor()
                fattest_corridor.stated_capacity -= 1
                theoretical_output = room.get_total_output()
                room.max_out_capacity = theoretical_output
                theoretical_input = room.get_total_input()
        else:
            room.max_out_capacity = theoretical_input
    elif theoretical_input > room.max_out_capacity:
        # reduce the input corridors capacity to match the room's actual max out capacity
        while theoretical_input > room.max_out_capacity:
            fattest_corridor = room.get_fattest_input_corridor()
            fattest_corridor.stated_capacity -= 1
            theoretical_input = room.get_total_input()

    for in_corridor in room.in_ways:
        input_room = in_corridor.from_room
        if input_room.index not in entrances:
            calculate_actual_throughput(input_room, entrances, exits)


def solution(entrances, exits, pathways):
    rooms = generate_room_network(exits, pathways)

    for exit_idx in exits:
        exit_room = rooms[exit_idx]
        calculate_actual_throughput(exit_room, entrances, exits)

    for exit_idx in exits:
        exit_room = rooms[exit_idx]
        calculate_actual_throughput(exit_room, entrances, exits)

    maximum_output = 0
    for exit_idx in exits:
        exit_room = rooms[exit_idx]
        maximum_output += exit_room.get_total_input()

    return maximum_output


def generate_room_network(exits, pathways):
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
    for exit_idx in exits:
        exit_room = rooms[exit_idx]
        exit_room.max_out_capacity = exit_room.get_total_input()
    return rooms
