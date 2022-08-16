"""
77. Combinations

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

from itertools import combinations
from typing import List


class Solution:

    def __init__(self):
        self.all_output: List[List[int]] = []

    def backtrack(self, n, k, cur_arr, index, result):

        if len(cur_arr) == k:
            result.append(cur_arr)
            return

        for ind in range(index, n + 1):
            self.backtrack(n, k, cur_arr + [ind], ind + 1, result)

    def recursiveSolution(self, n: int, k: int) -> List[List[int]]:
        # Runtime: 568 ms, faster than 50.39% of Python3 online submissions
        # Memory Usage: 15.1 MB, less than 70.64% of Python3 online submissions
        # recursively append values till len==k

        # if k == 1:
        #    return [[i] for i in range(1, n+1)]
        # if k == n:
        #    return [i for i in range(1, n+1)]

        result = []
        self.backtrack(n, k, [], 1, result)

        return result

    def pythonCheat(self, n: int, k: int) -> List[List[int]]:
        # Runtime: 80 ms, faster than 97.68% of Python3 online submissions
        # Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions
        # use default python method
        arr = list(range(1, n + 1))
        return combinations(arr, k)

    def backtrack2(self,
                   nums: List[int],
                   k: int,
                   cur_output: List[int]) -> None:
        """
        Backtrack solution using template
        """
        # print('*************************')
        # print('nums = ', nums)
        # print('cur_output = ', cur_output)
        # print('all_output = ', self.all_output)

        if len(cur_output) == k:
            self.all_output.append(cur_output.copy())
            return

        for ind, num in enumerate(nums):
            # use current candidate
            cur_output.append(num)

            # go deeper
            self.backtrack2(nums[ind + 1:], k, cur_output)

            # backtrack
            cur_output.pop()

        return

    def combine(self, n: int, k: int) -> List[List[int]]:
        # return self.recursiveSolution(n, k)
        # return self.pythonCheat(n, k)
        self.backtrack2(list(range(1, n+1)), k, [])
        return self.all_output
