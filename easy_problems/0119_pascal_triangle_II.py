"""
119. Pascal's Triangle II

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Examples:
Input: rowIndex = 3
Output: [1,3,3,1]

Input: rowIndex = 0
Output: [1]

Input: rowIndex = 1
Output: [1,1]
"""
from typing import List
from functools import lru_cache


class Solution:

    @lru_cache
    def get_value(self, i, j):
        if j == 0 or i == j:
            return 1
        return self.get_value(i - 1, j - 1) + self.get_value(i - 1, j)

    def getRowRecursively(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        arr = []
        for j in range(rowIndex + 1):
            val = self.get_value(rowIndex, j)
            arr.append(val)
            print(arr, val, rowIndex, j)
        return arr

    def getRow(self, rowIndex: int) -> List[int]:
        return self.getRowRecursively(rowIndex)
