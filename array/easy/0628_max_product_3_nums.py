"""
628. Maximum Product of Three Numbers

Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

Example 1:
Input: nums = [1,2,3]
Output: 6

Example 2:
Input: nums = [1,2,3,4]
Output: 24

Example 3:
Input: nums = [-1,-2,-3]
Output: -6
"""
from typing import List


class Solution:

    def sort_2_arrays(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]

        pos_nums = []
        neg_nums = []

        for num in nums:
            if num >= 0:
                pos_nums.append(num)
            if num < 0:
                neg_nums.append(num)

        cnt_pos = len(pos_nums)
        cnt_neg = len(neg_nums)

        if cnt_pos == 0:
            neg_nums_sorted = sorted(neg_nums)
            return neg_nums_sorted[-1] * neg_nums_sorted[-2] * neg_nums_sorted[-3]

        if cnt_neg > 1:
            neg_nums_sorted = sorted(neg_nums)
            pos_nums_sorted = sorted(pos_nums)

            var1 = neg_nums_sorted[0] * neg_nums_sorted[1] * pos_nums_sorted[-1]

            if cnt_pos < 3:
                return var1
            else:
                var2 = pos_nums_sorted[-1] * pos_nums_sorted[-2] * pos_nums_sorted[-3]
                if var2 > var1:
                    return var2
                else:
                    return var1
        else:
            pos_nums_sorted = sorted(pos_nums)
            return pos_nums_sorted[-1] * pos_nums_sorted[-2] * pos_nums_sorted[-3]

    def sort_simple(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        val1 = nums_sorted[-1] * nums_sorted[-2] * nums_sorted[-3]
        val2 = nums_sorted[0] * nums_sorted[1] * nums_sorted[-1]
        return max(val1, val2)

    def maximumProduct(self, nums: List[int]) -> int:
        # return self.sort_2_arrays(nums)  # accepted solution
        return self.sort_simple(nums)  # accepted solution
