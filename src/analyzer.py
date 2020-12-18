import numpy as np
from numba import jit

@jit(nopython=True, parallel=True)
def analyze(circs, img):
    rows = img.shape[0]
    cols = img.shape[1]
    count = 0
    for c in circs:
        count += 1
        c_x = c[0]
        c_y = c[1]
        rad = c[2]
        r = g = b = 0
        square = 0
        perimeter = 0
        for x in range(rows):
            for y in range(cols):
                if (x - c_x)**2 + (y - c_y)**2 <= rad*rad:
                    square += 1
                    r += img[x][y][0]
                    g += img[x][y][1]
                    b += img[x][y][2]

        _x = 0
        _y = 0
        for x in range(rows):
            for y in range(cols):
                if (x - c_x)**2 + (y - c_y)**2 <= rad*rad:
                    _x += x
                    _y += y
                    if ((x + 1 - c_x)**2 + (y - c_y)**2 > rad*rad or (x - 1 - c_x)**2 + (y - c_y)**2 > rad*rad
                        or (x - c_x)**2 + (y + 1 - c_y)**2 > rad*rad or (x - c_x)**2 + (y - 1 - c_y)**2 > rad*rad):
                        perimeter += 1

        print("circle №", count)
        print("x =", c_x, "y =", c_y)
        print("rad = ", rad)
        print("square = ", square)
        print("perimeter = ", perimeter)
        print("=======================")
