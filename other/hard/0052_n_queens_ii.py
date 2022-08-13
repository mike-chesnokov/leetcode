"""
52. N-Queens II

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such
that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example 1:
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

Example 2:
Input: n = 1
Output: 1

"""
from collections import defaultdict


class Solution:

    def __init__(self):
        self.under_attack = defaultdict(int)
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                           (1, 1), (-1, 1), (1, -1), (-1, -1)]

    def is_under_attack(self, row_ind: int, col_ind: int) -> bool:
        if (row_ind, col_ind) in self.under_attack and \
                self.under_attack[(row_ind, col_ind)] > 0:
            return True
        return False

    def place_queen(self, size: int, row_ind: int, col_ind: int) -> None:
        # add current cell
        self.under_attack[(row_ind, col_ind)] += 1

        for row_diff, col_diff in self.directions:
            # create new cell
            new_row = row_ind + row_diff
            new_col = col_ind + col_diff
            # go over current direction
            while new_row >= 0 and new_row < size and \
                    new_col >= 0 and new_col < size:
                self.under_attack[(new_row, new_col)] += 1
                new_row += row_diff
                new_col += col_diff

    def remove_queen(self, size: int, row_ind: int, col_ind: int) -> None:
        # remove current cell
        self.under_attack[(row_ind, col_ind)] -= 1

        for row_diff, col_diff in self.directions:
            # create new cell
            new_row = row_ind + row_diff
            new_col = col_ind + col_diff
            # go over current direction
            while new_row >= 0 and new_row < size and \
                    new_col >= 0 and new_col < size:
                self.under_attack[(new_row, new_col)] -= 1
                new_row += row_diff
                new_col += col_diff

    def backtrack(self, size: int, row_ind: int, cnt_queens: int) -> int:
        # iterate over columns
        for col_ind in range(size):
            # check if we could place the queen at this cell
            if self.is_under_attack(row_ind, col_ind):
                continue
            else:
                # mark attacking zone
                self.place_queen(size, row_ind, col_ind)

                # final case - last row
                if row_ind + 1 == size:
                    cnt_queens += 1
                else:
                    # go to the next row
                    cnt_queens = self.backtrack(size, row_ind + 1, cnt_queens)

                # clear attakcing zone from prev step
                self.remove_queen(size, row_ind, col_ind)

        return cnt_queens

    def totalNQueens(self, n: int) -> int:
        return self.backtrack(n, 0, 0)
