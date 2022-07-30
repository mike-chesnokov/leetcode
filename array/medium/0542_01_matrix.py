"""
542. 01 Matrix

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.

Example 1:
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]

Constraints:
    m == mat.length
    n == mat[i].length
    1 <= m, n <= 104
    1 <= m * n <= 104
    mat[i][j] is either 0 or 1.
    There is at least one 0 in mat.
"""
from typing import List


class Solution:

    def bfs(self, mat: List[List[int]],
            row_ind_: int, col_ind_: int,
            num_rows_: int, num_cols_: int) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = [(row_ind_, col_ind_)]
        visited = set()
        stack = []
        dist_to_zero = 0

        while queue:
            len_q = len(queue)
            dist_to_zero += 1
            # print('queue = ', queue)
            # print('stack = ', stack)
            # print('dist_to_zero = ', dist_to_zero)

            for _ in range(len_q):
                cur_row, cur_col = queue.pop(0)

                for row_diff, col_diff in directions:

                    new_row = cur_row + row_diff
                    new_col = cur_col + col_diff

                    if new_row < 0 or new_row >= num_rows_ or \
                            new_col < 0 or new_col >= num_cols_ or \
                            (new_row, new_col) in visited:
                        continue

                    # print('new_row = ', new_row, 'new_col = ', new_col)
                    # print('mat[new_row][new_col] =', mat[new_row][new_col])

                    if mat[new_row][new_col] == 0:
                        return dist_to_zero

                    visited.add((new_row, new_col))
                    # process queue
                    queue.append((new_row, new_col))

    def bfs_helper(self, mat: List[List[int]]) -> List[List[int]]:
        """
        iterate through all cells
        start bfs from "1"- find shortest way to "0"
        """
        num_rows = len(mat)
        num_cols = len(mat[0])
        result = []

        for row_ind in range(num_rows):
            result.append([])
            for col_ind in range(num_cols):
                if mat[row_ind][col_ind] != 0:
                    # print('*******************')
                    # print('result = ', result)
                    # print('row_ind = ', row_ind, 'col_ind = ', col_ind)
                    res = self.bfs(mat, row_ind, col_ind,
                                   num_rows, num_cols)
                    result[row_ind].append(res)
                    # print('result = ', result)
                else:
                    result[row_ind].append(0)
        return result

    def bfs_from_zeros(self, mat: List[List[int]]) -> List[List[int]]:
        """
        iterate through all cells, find zeros add them to queue
        other cells mark as 999999
        start bfs from "0"
        """
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        num_rows = len(mat)
        num_cols = len(mat[0])
        result = []  # save distances here
        queue = []  # first its is queue with zeros

        # append all zeros to queue
        for row_ind in range(num_rows):
            result.append([])
            for col_ind in range(num_cols):
                if mat[row_ind][col_ind] == 0:
                    # for zero distance = 0
                    result[row_ind].append(0)
                    # append zeros to queue
                    queue.append((row_ind, col_ind))
                else:
                    result[row_ind].append(999999)

        # start bfs from zeros
        while queue:
            cur_row, cur_col = queue.pop(0)
            for row_diff, col_diff in directions:

                new_row = cur_row + row_diff
                new_col = cur_col + col_diff

                if new_row < 0 or new_row >= num_rows or \
                        new_col < 0 or new_col >= num_cols:
                    continue
                # update distances
                if result[new_row][new_col] > result[cur_row][cur_col] + 1:
                    result[new_row][new_col] = result[cur_row][cur_col] + 1
                    queue.append((new_row, new_col))

        return result

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # return self.bfs_helper(mat)  # Time Limit
        return self.bfs_from_zeros(mat)  # Accepted

