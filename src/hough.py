import numpy as np
from numba import jit

@jit(nopython=True, parallel=True)
def hough_circles(input, circles):
    rows = input.shape[0]
    cols = input.shape[1]

    length=int(rows/2)
    radius = [i for i in range(5,length)]

    for r in radius:
        acc_cells = np.full((rows, cols), fill_value=0, dtype=np.uint64)

        for x in range(rows):
            for y in range(cols):
                if input[x][y] == 255:
                    for angle in range(0, 360):
                        b = y - round(r * np.sin(angle * np.pi / 180))
                        a = x - round(r * np.cos(angle * np.pi / 180))
                        if 0 <= a < rows and 0 <= b < cols:
                            acc_cells[a][b] += 1

        acc_cell_max = np.amax(acc_cells)

        if acc_cell_max > 150:
            for x in range(rows):
                for y in range(cols):
                    if acc_cells[x][y] < 150:
                        acc_cells[x][y] = 0
            for i in range(rows):
                for j in range(cols):
                    if 0 < i < rows - 1 and 0 < j < cols - 1 and acc_cells[i][j] >= 150:
                        avg_sum = np.float32((acc_cells[i][j] + acc_cells[i - 1][j] + acc_cells[i + 1][j] +
                                              acc_cells[i][j - 1] + acc_cells[i][j + 1] + acc_cells[i - 1][j - 1] +
                                              acc_cells[i - 1][j + 1] + acc_cells[i + 1][j - 1] + acc_cells[i + 1][
                                                  j + 1]) / 9)
                        if avg_sum >= 33:
                            circles.append((i, j, r))
                            acc_cells[i:i + 5, j:j + 7] = 0
