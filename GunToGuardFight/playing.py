from math import pi, cos, sin
from GunToGuardFight.graphics import *


class Ray:
    def __init__(self, x1, y1, x2, y2, length, course, reflection):
        self.start_x = x1
        self.start_y = y1
        self.end_x = x2
        self.end_y = y2
        self.length = length
        self.course = course
        self.reflection = reflection

    def get_end_point(self):
        return self.end_x, self.end_y


class CompoundRay:
    def __init__(self, ray):
        self.rays = list()
        self.rays.append(ray)
        self.total_length = ray.length
        self.active = True

    def add_ray(self, ray, max_overall_length):
        if self.total_length + ray.length <= max_overall_length:
            self.rays.append(ray)
            self.total_length += ray.length
            return True
        else:
            self.active = False
            return False

    def get_ray(self, index):
        return self.rays[index]


def does_intersect_target(origin, target, dx, dy):
    xdiff = target[0] - origin[0]
    ydiff = target[1] - origin[1]

    xmult = xdiff / dx
    ymult = ydiff / dy

    asda = 0

def generate_ray(d, origin, space, target):
    xplus = space[0] - origin[0]
    xminus = origin[0]
    yplus = space[1] - origin[1]
    yminus = origin[1]
    rad = ((d / 360) * (2 * pi))
    dx = round(cos(rad), 3)
    dy = round(sin(rad), 3)
    closest = ''
    reflected = None
    x_mult_factor = y_mult_factor = None

    does_intersect_target(origin, target, dx, dy)

    if dx > 0:
        x_mult_factor = round(xplus / dx, 3)
    elif dx < 0:
        x_mult_factor = round(xminus / dx, 3)
    else:
        x_mult_factor = 0

    if dy > 0:
        y_mult_factor = round(yplus / dy, 3)
    elif dy < 0:
        y_mult_factor = round(yminus / dy, 3)
    else:
        y_mult_factor = 0

    if abs(x_mult_factor) == abs(y_mult_factor):
        # corner
        closest = 'corner'
        reflected = 360 - d

    elif abs(y_mult_factor) == 0 or abs(y_mult_factor) > abs(x_mult_factor) > 0:
        if x_mult_factor < 0:
            closest = 'left'
            x_intersect = 0
            y_intersect = origin[1] - round(x_mult_factor * sin(rad), 3)
        else:
            closest = 'right'
            x_intersect = space[0]
            y_intersect = origin[1] + round(x_mult_factor * sin(rad), 3)

        if d < 180:
            reflected = 180 - d
        else:
            reflected = (360 - d) + 180

        ray = Ray(origin[0], origin[1], x_intersect, y_intersect, abs(x_mult_factor), d, reflected)
        return ray
    else:
        if y_mult_factor < 0:
            closest = 'top'
            x_intersect = origin[0] - round(y_mult_factor * cos(rad), 3)
            y_intersect = 0
        else:
            closest = 'bottom'
            x_intersect = origin[0] + round(y_mult_factor * cos(rad), 3)
            y_intersect = space[1]

        reflected = 360 - d
        ray = Ray(origin[0], origin[1], x_intersect, y_intersect, abs(y_mult_factor), d, reflected)
        return ray


def generate_rays(space, guard_pos, shooter_pos):
    compound_rays = list()
    for d in range(125, 360, 5):
        ray = generate_ray(d, guard_pos, space, shooter_pos)
        compound_rays.append(CompoundRay(ray))

    return compound_rays


def draw_rays(win, compound_rays, index, colour):
    for compound_ray in compound_rays:
        if compound_ray.active:
            ray = compound_ray.get_ray(index)
            l1 = Line(Point(ray.start_x, ray.start_y), Point(ray.end_x, ray.end_y))
            l1.setWidth(1)
            l1.setFill(colour)
            l1.draw(win)
    win.getMouse()


if __name__ == '__main__':
    ray_colours = {0: 'black', 1: 'red', 2: 'blue', 3: 'yellow'}
    guard_position = [185, 100]
    guard_room = [300, 275]
    shooter = [150,150]
    max_ray_length = 500
    compound_rays = generate_rays(guard_room, guard_position, shooter)
    win = GraphWin('Guard Room', 400, 375)
    eye1 = Circle(Point(150, 150), 5)
    eye1.setFill('yellow')
    eye1.draw(win)

    draw_rays(win, compound_rays, 0, 'black')

    for source_ray_index in range(0, 2):
        for compound_ray in compound_rays:
            if compound_ray.active:
                source_ray = compound_ray.get_ray(source_ray_index)
                ref_ray = generate_ray(source_ray.reflection, source_ray.get_end_point(), guard_room, shooter)
                compound_ray.add_ray(ref_ray, max_ray_length)

        draw_rays(win, compound_rays, source_ray_index + 1, ray_colours[source_ray_index + 1])

    win.close()
