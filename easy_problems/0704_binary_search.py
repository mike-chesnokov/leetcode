"""
704. Binary Search

Given a sorted (in ascending order) integer array nums of n elements and a target value, 
write a function to search target in nums. 
If target exists, then return its index, otherwise return -1.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Note:
    You may assume that all elements in nums are unique.
    n will be in the range [1, 10000].
    The value of each element in nums will be in the range [-9999, 9999].
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Runtime: 388 ms, faster than 9.52% of Python3 online submissions
        # Memory Usage: 15 MB, less than 52.03% of Python3 online submissions
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
