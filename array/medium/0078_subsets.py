"""
78. Subsets

Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Examples:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Input: nums = [0]
Output: [[],[0]]
"""
from typing import List
from itertools import combinations


class Solution:
    def __init__(self):
        self.result = []

    def backtracking(
            self,
            nums: List[int],
            cur_arr: List[int],  # current array
            cand_len: int,  # current target length
            start_ind: int  # current start index
    ) -> List[List[int]]:

        # print(cur_arr, cand_len, self.result)
        # base case: len of current array = len of candidates
        if len(cur_arr) == cand_len:
            self.result.append(cur_arr.copy())
            # print('result', self.result)
            return

            # take next elements from nums
        for ind in range(start_ind, len(nums)):
            # add element to current combination
            cur_arr.append(nums[ind])
            # go deeper to next elements
            self.backtracking(nums, cur_arr, cand_len, ind + 1)
            # backtrack
            cur_arr.pop()

    def helper_backtrack(self, nums: List[int]) -> List[List[int]]:
        # iterate over length of candidates
        for cand_len in range(len(nums) + 1):
            self.backtracking(nums, [], cand_len, 0)

        return self.result

    def built_in_combinations(self, nums: List[int]) -> List[List[int]]:
        """Using built-in method for combinations"""
        res = []

        for i in range(len(nums) + 1):
            for comb in combinations(nums, i):
                res.append(list(comb))

        return res

    def cascading(self, nums: List[int]) -> List[List[int]]:
        """Add 1 num for every previous resulst"""
        res = [[]]

        for num in nums:
            res += [cur + [num] for cur in res]

        return res

    def bitmask(self, nums: List[int]) -> List[List[int]]:
        """Using bitwise mask to generate candidates"""
        n = len(nums)
        res = []

        for i in range(2 ** n, 2 ** (n + 1)):
            bitmask = bin(i)[3:]

            res.append([nums[i] for i in range(n) if bitmask[i] == '1'])

        return res

    def subsets(self, nums: List[int]) -> List[List[int]]:
        # return self.cascading(nums)
        # return self.bitmask(nums)
        # return self.built_in_combinations(nums)
        return self.helper_backtrack(nums)
