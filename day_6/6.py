import sys

def read_input(path):
    file = open(path, "r")
    file_content = [list(x.strip()) for x in file.readlines()]
    file.close()
    return file_content

def get_guard(gmap):
    row_pos, col_pos, direction = 0, 0, '^'
    for row in range(len(gmap)):
        for col in range((row)):
            if gmap[row][col] not in ".#":
                row_pos = row
                col_pos = col
                direction = gmap[row][col]

    return (row_pos, col_pos, direction)

def move_guard(gmap, row, col, direction):
    nrow, ncol = row, col
    ndir = direction
    match direction:
        case '^': nrow -= 1; ndir = '>'
        case '>': ncol += 1; ndir = 'v'
        case 'v': nrow += 1; ndir = '<'
        case '<': ncol -= 1; ndir = '^'

    gmap[row][col] = 'X'

    if gmap[nrow][ncol] == '#': return move_guard(gmap, row, col, ndir)
    elif (nrow == 0 and direction == '^') or (nrow == (len(gmap) - 1) and direction == 'v') or (ncol == 0 and direction == '<') or (ncol == (len(gmap[0]) - 1)): print(nrow, ncol); return True

    return move_guard(gmap, nrow, ncol, direction)


def count_fields(gmap, value):
    count = 0
    for row in gmap:
        for col in row:
            if col == value:
                count += 1

    return count


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    content = read_input("input")
    guard = get_guard(content)
    move_guard(content, guard[0], guard[1], guard[2])
    print(count_fields(content, 'X') + 1)


