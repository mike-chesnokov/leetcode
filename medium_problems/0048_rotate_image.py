"""
48. Rotate Image

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
"""
from typing import List


class Solution:
    def rotate_4_numbers(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                temp = matrix[i][j]

                matrix[i][j] = matrix[n - 1 - j][i]
                # print((i, j), '=', (n-1-j, i))

                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                # print((n-1-j, i), '=', (n-1-i, n-1-j))

                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                # print((n-1-i, n-1-j), '=', (j, n-1-i))

                matrix[j][n - 1 - i] = temp
                # print((j, n-1-i), '=', (i, j))
                # print(matrix)

    def transpose(self, matrix: List[List[int]]):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def reverse(self, matrix: List[List[int]]):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]

    def rotate_transpose_reverse(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.reverse(matrix)
