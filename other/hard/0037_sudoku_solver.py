"""
37. Sudoku Solver

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

    Each of the digits 1-9 must occur exactly once in each row.
    Each of the digits 1-9 must occur exactly once in each column.
    Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

Example 1:
Input: board = [
["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],
["6","7","2","1","9","5","3","4","8"],
["1","9","8","3","4","2","5","6","7"],
["8","5","9","7","6","1","4","2","3"],
["4","2","6","8","5","3","7","9","1"],
["7","1","3","9","2","4","8","5","6"],
["9","6","1","5","3","7","2","8","4"],
["2","8","7","4","1","9","6","3","5"],
["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:

Constraints:
    board.length == 9
    board[i].length == 9
    board[i][j] is a digit or '.'.
    It is guaranteed that the input board has only one solution.
"""
from typing import List


class Solution:
    num_rows = 9
    num_cols = 9
    all_vals = set(map(str, list(range(1, 10))))
    square_map = {
        0: (0, 2),
        1: (3, 5),
        2: (6, 8)
    }

    def __init__(self):
        self.empty_cells = []

    def is_solved(self, cur_ind) -> bool:
        if len(self.empty_cells) == cur_ind:
            return True
        return False

    def get_avaliable_vals(self, board, row_ind, col_ind):
        # collect available vals from row and col
        available_vals = self.all_vals - set(board[row_ind]) - \
                         set([board[ind][col_ind] for ind in range(9)])

        # collect available vals from square
        row_limits = self.square_map[row_ind // 3]
        col_limits = self.square_map[col_ind // 3]
        board_square = [
            board[row][col]
            for row in range(row_limits[0], row_limits[1] + 1)
            for col in range(col_limits[0], col_limits[1] + 1)
        ]

        available_vals = available_vals - set(board_square)
        # print('board[row_ind] =', board[row_ind])
        # print('board[col_ind] =', [board[ind][col_ind] for ind in range(9)])
        # print('board_square =', board_square)
        # print('available_vals =', available_vals)

        return available_vals

    def backtrack(self, board: List[List[str]],
                  cur_ind: int,  # index of empty cells array
                  ) -> bool:
        # check if there are no empty cells
        if self.is_solved(cur_ind):
            return True

        row_ind, col_ind = self.empty_cells[cur_ind]
        # print('**************************')
        # print('cur_ind = ', cur_ind)
        # print('self.empty_cells[cur_ind] = ', self.empty_cells[cur_ind], '\n')
        # print('row_ind, col_ind = ', row_ind, col_ind, '\n')

        available_vals = self.get_avaliable_vals(board, row_ind, col_ind)

        for val in available_vals:

            # try to fill cell with current val
            board[row_ind][col_ind] = val

            if self.backtrack(board, cur_ind + 1):
                return True

            # backtrack
            board[row_ind][col_ind] = '.'

        return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # collect initial empty cells
        for row_ind in range(self.num_rows):
            for col_ind in range(self.num_cols):
                val = board[row_ind][col_ind]
                # add empty cell
                if val == '.':
                    self.empty_cells.append((row_ind, col_ind))

        self.backtrack(board, 0)
