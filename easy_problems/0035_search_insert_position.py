"""
35. Search Insert Position

Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:
Input: [1,3,5,6], 5
Output: 2

Example 2:
Input: [1,3,5,6], 2
Output: 1

Example 3:
Input: [1,3,5,6], 7
Output: 4

Example 4:
Input: [1,3,5,6], 0
Output: 0
"""
from typing import List


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """ 
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = (left + right)// 2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left

    def searchInsert2(self, nums: List[int], target: int) -> int:
        nums_len = len(nums)
        left_ind = 0
        right_ind = nums_len - 1

        if target > nums[-1]:
            return nums_len
        if target < nums[0]:
            return 0

        while left_ind < right_ind:

            mid = left_ind + (right_ind - left_ind) // 2

            print('ind', left_ind, mid, right_ind)
            print('arr', nums[left_ind], nums[mid], nums[right_ind])

            if target < nums[mid]:
                right_ind = mid
            if target > nums[mid]:
                left_ind = mid
            if target == nums[mid]:
                return mid
            if target == nums[left_ind]:
                return left_ind
            if target == nums[right_ind]:
                return right_ind
            if right_ind == left_ind + 1 \
                    and nums[left_ind] < target < nums[right_ind]:
                return right_ind

        return right_ind
