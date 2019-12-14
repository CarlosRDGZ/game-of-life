ROWS = 10
COLUMNS = 10


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


def main():
    cells = create_cells(ROWS, COLUMNS)
    get_number_of_neighbors(4, 4, cells)

    for row in cells:
        for cell in row:
            print(cell['neighbors'], end='')
        print()


if __name__ == '__main__':
    main()
