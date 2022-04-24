"""
33. Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. 
If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

class Solution(object):
    
    def binary_search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right)//2
            mid_el = nums[mid]

            if target < mid_el:
                right = mid
            if target > mid_el:
                left = mid + 1
            if target == mid_el:
                return mid
        return left

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if target not in nums:
            return -1

        left, right = 0, len(nums)-1
        left_el = nums[left]
        right_el = nums[right]
        break_ind = 0

        while left_el > right_el:

            mid = (left + right)//2

            left_el = nums[left]
            right_el = nums[right]        
            mid_el = nums[mid]

            if left_el < mid_el:
                left = mid
            if left_el > mid_el:
                right = mid
            if left_el == mid_el:
                break_ind = left + 1
                break
                
        if break_ind == 0:
            ind = self.binary_search(nums, target)
        else:
            if target in nums[:break_ind]:
                ind = self.binary_search(nums[:break_ind], target)
            else:
                ind = self.binary_search(nums[break_ind:], target)
                ind += break_ind

        return ind