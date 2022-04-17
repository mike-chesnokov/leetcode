"""
136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one.
Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Examples:
Input: nums = [2,2,1]
Output: 1

Input: nums = [4,1,2,1,2]
Output: 4

Input: nums = [1]
Output: 1
"""
from typing import List
from collections import Counter


class Solution:
    def counter(self, nums: List[int]) -> int:
        """With Counter"""
        nums_cnt = Counter(nums)
        for el in nums_cnt:
            if nums_cnt[el] == 1:
                return el

    def xor_operator(self, nums: List[int]) -> int:
        """With XOR operator:  1 xor 1 = 0, 2 xor 2 = 0, 3 xor 3 = 0 """
        res = 0
        for el in nums:
            res ^= el
        return res
