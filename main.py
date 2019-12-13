ROWS = 20
COLUMNS = 20


def create_cells(rows, columns):
    cells = []
    for row in range(rows):
        cells.append([])
        for col in range(columns):
            cells[row].append({
                'isAlive': False,
                'neighbors': 0
            })
    return cells


def main():
    cells = create_cells(ROWS, COLUMNS)

    for row in cells:
        for cell in row:
            print(cell['neighbors'], end='')
        print()


if __name__ == '__main__':
    main()