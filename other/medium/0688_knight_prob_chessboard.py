"""
688. Knight Probability in Chessboard
On an n x n chessboard, a knight starts at the cell (row, column) and attempts to make exactly k moves.
 The rows and columns are 0-indexed, so the top-left cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).

A chess knight has eight possible moves it can make, as illustrated below.
Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.

Each time the knight is to move, it chooses one of eight possible moves uniformly at random
(even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly k moves or has moved off the chessboard.

Return the probability that the knight remains on the board after it has stopped moving.

Example 1:
Input: n = 3, k = 2, row = 0, column = 0
Output: 0.06250
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.

Example 2:
Input: n = 1, k = 0, row = 0, column = 0
Output: 1.00000

Constraints:
    1 <= n <= 25
    0 <= k <= 100
    0 <= row, column <= n - 1
"""

class Solution:

    def __init__(self):
        self.num_in = 0
        self.memo = {}

    def get_candidates(self, row: int, col: int) -> List[int]:
        cand_list = []
        directions = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]

        for dx, dy in directions:
            cand_list.append((row + dx, col + dy))

        return cand_list

    def is_in_board(self, size: int, row: int, col: int):
        if row >= 0 and col >= 0 and \
                row <= size - 1 and col <= size - 1:
            return True
        else:
            return False

    def backtracking(self, size: int, num_moves: int, row: int, col: int):
        """
        Check all possible variants with backtracking
        """
        if num_moves == 0:
            self.num_in += 1
            return

        for cand_row, cand_col in self.get_candidates(row, col):
            if self.is_in_board(size, cand_row, cand_col):
                self.backtracking(size, num_moves - 1, cand_row, cand_col)

    def dfs(self, size: int, num_moves: int, row: int, col: int) -> float:
        """
        Recursive dfs solution
        """
        # memorization
        if (num_moves, row, col) in self.memo:
            return self.memo[(num_moves, row, col)]

        # final variant inside board
        if num_moves == 0:
            return 1

        num_in_board = 0

        for cand_row, cand_col in self.get_candidates(row, col):
            if self.is_in_board(size, cand_row, cand_col):
                num_in_board += self.dfs(size, num_moves - 1, cand_row, cand_col)

        self.memo[(num_moves, row, col)] = num_in_board

        return num_in_board

    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        if k == 0:
            return 1.

        if n == 1:
            return 0.

        # self.backtracking(n, k, row, column)  # Time Limit Exceeded
        # return  self.num_in/ 8**k

        return self.dfs(n, k, row, column) / 8 ** k  # Accepted
