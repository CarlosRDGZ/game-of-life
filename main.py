import os
import time
import random

ROWS = 20
COLUMNS = 20
random.seed(1)


def create_cells(rows, columns):
    cells = []
    for row in range(rows):
        cells.append([])
        for col in range(columns):
            cells[row].append(False)
    return cells


def get_number_of_neighbors(cell_row, cell_col, cells):
    neighbors = 0
    most_left_column: int = 0
    most_right_column = ROWS - 1

    if cell_col > 0:
        if cells[cell_row][cell_col - 1]:
            neighbors += 1
        most_left_column = cell_col - 1

    if cell_col < ROWS - 1:
        if cells[cell_row][cell_col + 1]:
            neighbors += 1
        most_right_column = cell_col + 1

    if cell_row > 0:
        for col in range(most_left_column, most_right_column + 1):
            if cells[cell_row - 1][col]:
                neighbors += 1

    if cell_row < ROWS - 1:
        for col in range(most_left_column, most_right_column + 1):
            if cells[cell_row + 1][col]:
                neighbors += 1

    return neighbors


def should_live(cell_row, cell_col, cells):
    is_alive = cells[cell_row][cell_col]
    neighbors = get_number_of_neighbors(cell_row, cell_col, cells)

    if is_alive and 2 <= neighbors <= 3:
        return True
    elif not is_alive and neighbors == 3:
        return True
    return False


def big_bang(cells):
    total_live_cells = ROWS * COLUMNS / 2
    while total_live_cells > 0:
        row = random.randint(0, ROWS - 1)
        col = random.randint(0, COLUMNS - 1)
        if not cells[row][col]:
            cells[row][col] = True
            total_live_cells -= 1


def main():
    current_cells = create_cells(ROWS, COLUMNS)
    future_cells = create_cells(ROWS, COLUMNS)

    big_bang(current_cells)

    while True:
        os.system('clear')

        for row in range(ROWS):
            for col in range(COLUMNS):
                future_cells[row][col] = should_live(row, col, current_cells)

        for row in current_cells:
            for cell in row:
                print(' • ' if cell else '   ', end='')
            print()

        current_cells, future_cells = future_cells, current_cells

        time.sleep(1)


if __name__ == '__main__':
    main()
