"""
240. Search a 2D Matrix II

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix.
This matrix has the following properties:
    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.

Example 1:
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

Example 2:
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= n, m <= 300
    -109 <= matrix[i][j] <= 109
    All the integers in each row are sorted in ascending order.
    All the integers in each column are sorted in ascending order.
    -109 <= target <= 109

"""
from typing import List

import numpy as np


class Solution:

    def recursively_3checks(self, matrix: np.array, target: int) -> bool:
        """
        Recursively divide matrix to 4 parts by middle point
        and take 3 of matrices to recursion
        """
        num_rows, num_cols = matrix.shape
        # print(matrix)
        # print(num_rows, num_cols)
        # base case - empty matrix
        if num_rows == 0 or num_cols == 0:
            return False
        # base case - matrix with 1 element
        if num_rows == 1 and num_cols == 1:
            if matrix[0, 0] == target:
                return True
            else:
                return False

        if num_rows % 2 == 0:
            pivot_ind = num_rows // 2 - 1
        else:
            pivot_ind = num_rows // 2

        if num_cols % 2 == 0:
            pivot_col = num_cols // 2 - 1
        else:
            pivot_col = num_cols // 2

        # base case - target found
        if target == matrix[pivot_ind, pivot_col]:
            return True

        if target < matrix[pivot_ind, pivot_col]:
            # top left matrix
            res1 = self.recursively_3checks(matrix[:pivot_ind + 1, :pivot_col + 1], target)
            # bottom left matrix
            res2 = self.recursively_3checks(matrix[pivot_ind + 1:, :pivot_col + 1], target)
            # top right matrix
            res3 = self.recursively_3checks(matrix[:pivot_ind + 1, pivot_col + 1:], target)

        elif target > matrix[pivot_ind, pivot_col]:
            # bottom right matrix
            res1 = self.recursively_3checks(matrix[pivot_ind + 1:, pivot_col + 1:], target)
            # bottom left matrix
            res2 = self.recursively_3checks(matrix[pivot_ind + 1:, :pivot_col + 1], target)
            # top right matrix
            res3 = self.recursively_3checks(matrix[:pivot_ind + 1, pivot_col + 1:], target)

        return res1 or res2 or res3

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.recursively_3checks(np.array(matrix), target)
