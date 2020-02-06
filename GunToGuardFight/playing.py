from math import pi, cos, sin


class Ray:
    def __init__(self, x1, y1, x2, y2, length, course, reflection):
        self.start_x = x1
        self.start_y = y1
        self.end_x = x2
        self.end_y = y2
        self.length = length
        self.course = course
        self.reflection = reflection


def generate_rays(space, guard_pos):
    xplus = space[0] - guard_pos[0]
    xminus = guard_pos[0]
    yplus = space[1] - guard_pos[1]
    yminus = guard_pos[1]

    rays = list()

    for d in range(0, 360, 15):
        rad = ((d / 360) * (2 * pi))
        dx = round(cos(rad), 3)
        dy = round(sin(rad), 3)
        closest = ''
        reflected = None
        x_mult_factor = y_mult_factor = None

        if dx > 0:
            x_mult_factor = round(xplus / dx, 3)
        elif dx < 0:
            x_mult_factor = round(xminus / dx, 3)
        else:
            x_mult_factor = 1E6

        if dy > 0:
            y_mult_factor = round(yplus / dy, 3)
        elif dy < 0:
            y_mult_factor = round(yminus / dy, 3)
        else:
            y_mult_factor = 1E6

        if abs(x_mult_factor) == abs(y_mult_factor):
            # corner
            closest = 'corner'
            reflected = 360 - d

        elif abs(x_mult_factor) < abs(y_mult_factor):
            if x_mult_factor < 0:
                closest = 'left'
                x_intersect = 0
                y_intersect = guard_pos[1] - round(x_mult_factor * sin(rad), 3)

            else:
                closest = 'right'
                x_intersect = space[0]
                y_intersect = guard_pos[1] + round(x_mult_factor * sin(rad), 3)

            if d < 180:
                reflected = 180 - d
            else:
                reflected = (360 - d) + 180

            ray = Ray(guard_pos[0], guard_pos[1], x_intersect, y_intersect, abs(x_mult_factor), d, reflected)
            rays.append(ray)
        else:
            if y_mult_factor < 0:
                closest = 'top'
                x_intersect = guard_pos[0] - round(y_mult_factor * cos(rad), 3)
                y_intersect = 0
            else:
                closest = 'bottom'
                x_intersect = guard_pos[0] + round(y_mult_factor * cos(rad), 3)
                y_intersect = space[1]

            reflected = 360 - d
            ray = Ray(guard_pos[0], guard_pos[1], x_intersect, y_intersect, abs(y_mult_factor), d, reflected)
            rays.append(ray)

        print('Deg: {0} Rad: {1} dx: {2} dy: {3} - closest={4} (xd:{5} yd:{6} - reflected: {7})'.format(d,
                                                                                                        rad,
                                                                                                        dx,
                                                                                                        dy,
                                                                                                        closest,
                                                                                                        x_mult_factor,
                                                                                                        y_mult_factor,
                                                                                                        reflected))
    return rays


if __name__ == '__main__':
    rays = generate_rays([3, 2], [2, 1])
    print (rays)
