"""
81. Search in Rotated Sorted Array II

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. 
If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
"""

class Solution:
    
    def binary_search(self, nums: List[int], target: int):
        
        nums_len = len(nums)
        
        if nums_len == 0:
            return -1
        left, right = 0, nums_len
        
        while left < right - 1:
            
            middle = left + (right-left)//2
            
            if target < nums[middle]:
                right = middle
            else:
                left = middle
        
        return left if nums[left] == target else -1 
    
    def search(self, nums: List[int], target: int) -> bool:
        
        nums_len = len(nums)
        
        if nums_len == 0:
            return False
        if nums_len == 1:
            return nums[0] == target
        if nums_len == 2:
            return nums[0] == target or nums[1] == target

        break_ind = nums_len
        for ind in range(nums_len - 1):
            if nums[ind] > nums[ind + 1]:
                break_ind = ind
                break
        
        left_nums = nums[:break_ind+1]
        right_nums = nums[break_ind+1:]
        
        left_ind = self.binary_search(left_nums, target)
        right_ind = self.binary_search(right_nums, target)
        
        return True if left_ind > -1 or right_ind > -1 else False
