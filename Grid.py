import numpy as np
from random import randint


class Grid:

    def __init__(self, wid, length):
        self.wid = wid
        self.length = length
        self.board = np.full((self.wid, self.length), 0)
        self.gen = 1
        self.half_board = []

    def half_gen(self):
        """
        Creates a sort of "rounded" array of arrays from our self.board. This func makes it so that the last row with index of [-1] can easily
        acces the row of index [0], by appending/inserting a row after it. This also works for the first row, and for the columns of indexes [0] and [-1].
        Visualization:
        [[0,1,2],       [[8, 6,7,8, 6],
         [3,4,5],   -->  [2, 0,1,2, 0],
         [6,7,8]]        [5, 3,4,5, 3],
                         [8, 6,7,8, 6],
                         [2, 0,1,2, 0]]
        :return: None
        """
        self.half_board = self.board.copy()
        self.half_board = np.append(self.half_board, [self.half_board[0, :]], axis=0)
        self.half_board = np.insert(self.half_board, 0, [self.half_board[-2, :]], axis=0)
        self.half_board = np.append(self.half_board,  [[i] for i in self.half_board[:, 0]], axis=1)
        self.half_board = np.insert(self.half_board, 0, [self.half_board[:, -2]], axis=1)

    def count_neighbours(self, row, col):
        """
        Counts the living neighbours of a cell in a specified position.
        :param row: Index of a row.
        :param col: Index of a column.
        :return:
        """
        temp = self.half_board[row:row + 3, col:col + 3].copy()
        temp[1, 1] = 0
        return np.count_nonzero(temp == 1)

    def __setitem__(self, key: tuple, value):
        self.board[key[0], key[1]] = value

    def __str__(self):
        return "\n".join([str(i) for i in self.board])

    def update(self, cords: set):
        """
        Sets cells of given coordination's to a "living" state.
        :param cords: Set of tuples (coordination's) of two integers (row,col).
        :return: None
        """
        self.board = np.full((self.wid, self.length), 0)
        for pos in cords:
            self.board[pos[0], pos[1]] = 1

    def next_gen(self):
        """
        Creates a new generation of Conway's game of life from our self.board.
        :return: None
        """
        self.gen += 1
        self.half_gen()
        cords = set()
        for row in range(1, self.wid + 1):
            for col in range(1, self.length + 1):
                neigh = self.count_neighbours(row-1, col-1)
                if self.half_board[row, col] == 1 and (neigh == 2 or neigh == 3): cords.add((row-1,col-1))
                elif self.half_board[row, col] == 0 and neigh == 3: cords.add((row-1,col-1))
        self.update(cords)

    def randomizer(self):
        """
        Sets random cells in self.board to a "living" state.
        :return: None
        """
        for row in range(self.wid):
            for col in range(self.length):
                self.board[row,col] = randint(0,1)

    def get_cords(self):
        """
        Returns coordinations of living cells.
        :return: List of lists.
        """
        cords = np.argwhere(self.board>0)
        return cords
