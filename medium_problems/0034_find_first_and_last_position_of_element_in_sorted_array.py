"""
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, f
ind the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Constraints:

    0 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
    nums is a non decreasing array.
    -10^9 <= target <= 10^9
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_len = len(nums)
        if nums_len == 0:
            return [-1, -1]

        left, right = 0, nums_len - 1

        while left <= right:
            mid = (left + right)//2
            el_mid = nums[mid]
            if target <= el_mid:
                right = mid - 1
            else:
                left = mid + 1    
        ind_left = left
        
        left, right = 0, nums_len - 1
        while left <= right:
            mid = (left + right)//2
            el_mid = nums[mid]

            if target < el_mid:
                right = mid - 1
            else:
                left = mid + 1

        if ind_left > right:
            return [-1, -1]
        
        return [ind_left, right]
