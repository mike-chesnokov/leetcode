"""
494. Target Sum

You are given an integer array nums and an integer target.
You want to build an expression out of nums by adding one of the symbols '+' and '-'
before each integer in nums and then concatenate all the integers.

    For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1
    and concatenate them to build the expression "+2-1".

Return the number of different expressions that you can build, which evaluates to target.

Example 1:
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

Example 2:
Input: nums = [1], target = 1
Output: 1

Constraints:

    1 <= nums.length <= 20
    0 <= nums[i] <= 1000
    0 <= sum(nums[i]) <= 1000
    -1000 <= target <= 1000
"""

from typing import List


class Solution:

    def __init__(self):
        self.cnt = 0
        self.cache = {}

    def recusrsion(self, nums: List[int], target: int, cur_sum: int, cur_ind: int) -> None:
        """
        Brute force recursion - O(2^N)
        """
        # print('cur_sum = ', cur_sum, 'cur_ind = ', cur_ind)
        if cur_ind == len(nums):
            if cur_sum == target:
                self.cnt += 1
            return

        num = nums[cur_ind]

        for var in [num, -1 * num]:
            self.recusrsion(nums, target, cur_sum + var, cur_ind + 1)

    def recusrsion_memo(self, nums: List[int], target: int,
                        cur_sum: int, cur_ind: int) -> int:
        """
        Recursion + memorization (cache)
        """
        # print('cur_sum = ', cur_sum, 'cur_ind = ', cur_ind)
        if cur_ind == len(nums):
            if cur_sum == target:
                return 1
            else:
                return 0
        # get result from cache
        if (cur_sum, cur_ind) in self.cache:
            return self.cache[(cur_sum, cur_ind)]

        # iterate through variants
        num = nums[cur_ind]
        res = 0
        for var in [num, -1 * num]:
            if (cur_sum + var, cur_ind + 1) not in self.cache:
                cur_res = self.recusrsion_memo(nums, target, cur_sum + var, cur_ind + 1)
                self.cache[(cur_sum + var, cur_ind + 1)] = cur_res
            else:
                cur_res = self.cache[(cur_sum + var, cur_ind + 1)]
            res += cur_res
        return res

    def recusrsion_memo2(self, nums: List[int], target: int,
                         cur_sum: int, cur_ind: int) -> int:
        """
        Recursion + memorization, cleaner
        """
        # print('cur_sum = ', cur_sum, 'cur_ind = ', cur_ind)
        if cur_ind == len(nums):
            if cur_sum == target:
                return 1
            else:
                return 0

        # get result from cache
        if (cur_sum, cur_ind) in self.cache:
            return self.cache[(cur_sum, cur_ind)]

        # result - sum of 2 variants "cur_sum +- num"
        num = nums[cur_ind]
        res = self.recusrsion_memo(nums, target, cur_sum + num, cur_ind + 1) + \
            self.recusrsion_memo(nums, target, cur_sum - num, cur_ind + 1)

        self.cache[(cur_sum, cur_ind)] = res

        return res

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # self.recusrsion(nums, target, 0, 0) # Time limit
        # return self.cnt
        # return self.recusrsion_memo(nums, target, 0, 0)  # accepted
        return self.recusrsion_memo2(nums, target, 0, 0)  # accepted
