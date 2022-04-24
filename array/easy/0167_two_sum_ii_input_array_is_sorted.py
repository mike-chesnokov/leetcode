"""
167. Two Sum II - Input array is sorted

Given an array of integers that is already sorted in ascending order, 
find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, 
where index1 must be less than index2.

Note:

    Your returned answers (both index1 and index2) are not zero-based.
    You may assume that each input would have exactly one solution and you may not use the same element twice.

Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""

class Solution:
    
    def twoPointers(self, numbers: List[int], target: int) -> List[int]:
        # use two pointers: start of array and end of array
        # Runtime: 68 ms, faster than 52.11% of Python3 online submissions
        # Memory Usage: 14.2 MB, less than 83.46% of Python3 online submissions 
        
        nums_len = len(numbers)
        
        if nums_len < 2:
            return None, None
        
        start = 0
        end = nums_len - 1
        
        while start != end:
            
            res = numbers[start] + numbers[end]
            
            if res == target:
                return start + 1, end + 1
            
            if res > target:
                end -= 1
                
            if res < target:
                start += 1
                
        return None, None
        
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        return self.twoPointers(numbers, target)
