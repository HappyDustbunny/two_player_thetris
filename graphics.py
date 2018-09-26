""" Graphics for Two Player Tetris """

from vpython import box, color, compound, random, sleep, scene, vector


def main():
    delta_t = .2
    columns, rows = 10, 24
    board = draw_board(columns, rows)
    first = Tetramino(0, 0)
    # first.update_tetramino('I', 'Horizontal')
    for shape in ['T', 'I', 'O', 'S', 'Z', 'J', 'L']:
        first(0, 0, shape, '0')
        sleep(delta_t)
        first(0, 0, shape, '1')
        sleep(delta_t)
        first(0, 0, shape, '2')
        sleep(delta_t)
        first(0, 0, shape, '3')
        sleep(delta_t)
        i = 0
    for _ in range(0, 190, 10):
        i += 1
        i %= 4
        print(i)
        first(10, 200 - _, 'T', str(i))
        sleep(delta_t)
    # x_coordinates, y_coordinates = list(range(columns)), list(range(rows))
    # board_status = {(x, y): (True, color.cyan, 1) for x in x_coordinates for y in y_coordinates}
    # update_board(board, board_status)
    # sleep(1)
    # change_cube_state(board, 1, 2, color.red, 1, True)
    # while True:
    #     board_status = {(x, y): (True, vector(random(), random(), random()), 1) for x in x_coordinates for y in
    #                     y_coordinates}
    #     update_board(board, board_status)
    #     sleep(0.1)


class Tetramino:
    """ Types I, O, S, Z, T, J, L """

    def __init__(self, x, y):
        self.x_pos = 10 * x
        self.y_pos = 10 * y
        self.shape = 'O'
        self.orientation = '1'
        self.box1 = box(pos=vector(x, y, 0), height=8, width=8, length=8)
        self.box2 = box(pos=vector(x, y, 0), height=8, width=8, length=8)
        self.box3 = box(pos=vector(x, y, 0), height=8, width=8, length=8)
        self.box4 = box(pos=vector(x, y, 0), height=8, width=8, length=8)

    def __call__(self, x, y, shape, orientation='0'):
        self.shape = shape
        self.box1.pos = vector(x, y, 0)
        self.box2.pos = self.box1.pos
        self.box3.pos = self.box1.pos
        self.box4.pos = self.box1.pos
        if shape == 'I' and orientation in '02':
            self.box2.pos += vector(10, 0, 0)
            self.box3.pos += vector(20, 0, 0)
            self.box4.pos += vector(30, 0, 0)
        elif shape == 'I' and orientation in '13':
            self.box2.pos += vector(0, 10, 0)
            self.box3.pos += vector(0, 20, 0)
            self.box4.pos += vector(0, 30, 0)
        elif shape == 'J' and orientation in '0':
            self.box2.pos += vector(10, 0, 0)
            self.box3.pos += vector(10, 10, 0)
            self.box4.pos += vector(10, 20, 0)
        elif shape == 'J' and orientation in '1':
            self.box1.pos += vector(20, 0, 0)
            self.box2.pos += vector(20, 10, 0)
            self.box3.pos += vector(10, 10, 0)
            self.box4.pos += vector(0, 10, 0)
        elif shape == 'J' and orientation in '2':
            self.box2.pos += vector(0, 10, 0)
            self.box3.pos += vector(0, 20, 0)
            self.box4.pos += vector(10, 20, 0)
        elif shape == 'J' and orientation in '3':
            self.box2.pos += vector(10, 0, 0)
            self.box3.pos += vector(20, 0, 0)
            self.box4.pos += vector(0, 10, 0)
        elif shape == 'L' and orientation in '0':
            self.box2.pos += vector(10, 0, 0)
            self.box3.pos += vector(20, 0, 0)
            self.box4.pos += vector(20, 10, 0)
        elif shape == 'L' and orientation in '1':
            self.box1.pos += vector(10, 0, 0)
            self.box2.pos += vector(10, 10, 0)
            self.box3.pos += vector(10, 20, 0)
            self.box4.pos += vector(0, 20, 0)
        elif shape == 'L' and orientation in '2':
            self.box2.pos += vector(0, 10, 0)
            self.box3.pos += vector(10, 10, 0)
            self.box4.pos += vector(20, 10, 0)
        elif shape == 'L' and orientation in '3':
            self.box2.pos += vector(10, 0, 0)
            self.box3.pos += vector(0, 10, 0)
            self.box4.pos += vector(0, 20, 0)
        if shape == 'S' and orientation in '02':
            self.box2.pos += vector(10, 0, 0)
            self.box3.pos += vector(10, 10, 0)
            self.box4.pos += vector(20, 10, 0)
        elif shape == 'S' and orientation in '13':
            self.box1.pos += vector(10, 0, 0)
            self.box2.pos += vector(10, 10, 0)
            self.box3.pos += vector(0, 10, 0)
            self.box4.pos += vector(0, 20, 0)
        if shape == 'Z' and orientation in '02':
            self.box2.pos += vector(0, 10, 0)
            self.box3.pos += vector(10, 10, 0)
            self.box4.pos += vector(10, 20, 0)
        elif shape == 'Z' and orientation in '13':
            self.box1.pos += vector(0, 10, 0)
            self.box2.pos += vector(10, 10, 0)
            self.box3.pos += vector(10, 0, 0)
            self.box4.pos += vector(20, 0, 0)
        elif shape == 'O':
            self.box2.pos += vector(10, 0, 0)
            self.box3.pos += vector(0, 10, 0)
            self.box4.pos += vector(10, 10, 0)
        elif shape == 'T' and orientation == '0':
            self.box2.pos += vector(10, 0, 0)
            self.box3.pos += vector(20, 0, 0)
            self.box4.pos += vector(10, 10, 0)
        elif shape == 'T' and orientation == '1':
            self.box1.pos += vector(10, 0, 0)
            self.box2.pos += vector(10, 10, 0)
            self.box3.pos += vector(10, 20, 0)
            self.box4.pos += vector(0, 10, 0)
        elif shape == 'T' and orientation == '2':
            self.box1.pos += vector(10, 0, 0)
            self.box2.pos += vector(0, 10, 0)
            self.box3.pos += vector(10, 10, 0)
            self.box4.pos += vector(20, 10, 0)
        elif shape == 'T' and orientation == '3':
            self.box2.pos += vector(0, 10, 0)
            self.box3.pos += vector(0, 20, 0)
            self.box4.pos += vector(10, 10, 0)


def draw_board(columns, rows):
    """ The board is a dictionary of cubes with coordinates as keys """
    scene.center = vector(int(10 * (columns - 1) / 2), int(10 * rows / 2), 0)
    x_coordinates, y_coordinates = list(range(columns)), list(range(rows))
    board = {(x, y): box(pos=vector(10 * x, 10 * y, 0), height=8, width=8, length=8, opacity=0.2)
             for x in x_coordinates for y in y_coordinates}
    board[(-1, -1)] = columns, rows  # Board size gets stored in the board with key (-1, -1)

    return board


def change_cube_state(board, x_coordinate, y_coordinate, colour=color.white, opacity=1, visible=True):
    item = board.get((x_coordinate, y_coordinate))
    item.visible = visible
    item.opacity = opacity
    item.color = colour


def update_board(board, board_status):
    columns, rows = board.get((-1, -1))  # Board size is stored in the board with key (-1, -1)
    for y in range(rows):
        for x in range(columns):
            cube = board.get((x, y))
            cube.visible, cube.color, cube.opacity = board_status.get((x, y))


if __name__ == '__main__':
    main()