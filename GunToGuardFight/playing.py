from math import asin, acos, atan, pi, cos, sin

dims = [400, 400]
gpos = [200, 200]

xplus = dims[0] - gpos[0]
xminus = gpos[0]

yplus = dims[1] - gpos[1]
yminus = gpos[1]

for d in range(0, 360, 1):
#for d in [0, 90, 180, 270]:
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
        else:
            closest = 'right'

        if d < 180:
            reflected = 180 - d
        else:
            reflected = (360 - d) + 180
    else:
        if y_mult_factor < 0:
            closest = 'top'
        else:
            closest = 'bottom'
        reflected = 360 - d
    print('Deg: {0} Rad: {1} dx: {2} dy: {3} - closest={4} (xd:{5} yd:{6} - reflected: {7})'.format(d,
                                                                                                    rad,
                                                                                                    dx,
                                                                                                    dy,
                                                                                                    closest,
                                                                                                    x_mult_factor,
                                                                                                    y_mult_factor,
                                                                                                    reflected))
