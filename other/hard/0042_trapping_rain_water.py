"""
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it is able to trap after raining.

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""

class Solution:
    
    def trapBruteForce(self, height: List[int]) -> int:
        # Runtime: 2096 ms, faster than 5.00% of Python3 online submissions
        # Memory Usage: 14.3 MB, less than 99.35% of Python3 online submissions
        # simply find max every iteration of array
        water = 0
        height_len = len(height)
        
        for ind in range(1, height_len - 1):
            # find max to the left and to the right of index
            left_max = max(height[:ind])
            right_max = max(height[ind+1:])
            # min of left and right maximums is the upper bound of water
            # height[ind] - lower bound of water
            water += max(min(left_max, right_max) - height[ind], 0)
            
        return water
    
    def trapMaxCalculations(self, height: List[int]) -> int:
        # Runtime: 60 ms, faster than 38.32% of Python3 online submissions
        # Memory Usage: 15.6 MB, less than 5.01% of Python3 online submissions 
        # use dicts to precalculate and save left and right maximums 
        water = 0
        
        height_len = len(height)
        if height_len == 0:
            return water
        
        # calculate left maximums
        left_max_dict = {}
        left_max_dict[0] = height[0]
        for ind in range(1, height_len - 1):
            left_max_dict[ind] = max(left_max_dict[ind - 1], height[ind])
        
        # calculate right maximums    
        right_max_dict = {}
        right_max_dict[height_len - 1] = height[height_len - 1]
        for ind in range(height_len - 2, 0, -1):
            right_max_dict[ind] = max(right_max_dict[ind + 1], height[ind])       
        
        # result calculation
        for ind in range(1, height_len - 1):
            left_max = left_max_dict[ind]
            right_max = right_max_dict[ind]
            water += max(min(left_max, right_max) - height[ind], 0)
            
        return water
    
    def trapMaxCalculations2(self, height: List[int]) -> int:
        # Runtime: 56 ms, faster than 54.45% of Python3 online submissions
        # Memory Usage: 15.4 MB, less than 5.01% of Python3 online submissions
        # use dicts to precalculate and save left and right maximums 
        water = 0
        
        height_len = len(height)
        if height_len == 0:
            return water
        
        # calculate right and left maximums in one pass
        left_max_dict = {}
        right_max_dict = {}
        
        left_max_dict[0] = height[0]
        right_max_dict[height_len - 1] = height[height_len - 1]
        
        for ind in range(1, height_len - 1):
            left_max_dict[ind] = max(left_max_dict[ind - 1], 
                                     height[ind])
            right_max_dict[height_len - 1 - ind] = max(right_max_dict[height_len - ind], 
                                                       height[height_len - 1 - ind])    
        
        # result calculation
        for ind in range(1, height_len - 1):
            left_max = left_max_dict[ind]
            right_max = right_max_dict[ind]
            water += max(min(left_max, right_max) - height[ind], 0)
            
        return water
    
    def trap(self, height: List[int]) -> int:
        # return self.trapBruteForce(height)
        # return self.trapMaxCalculations(height)
        return self.trapMaxCalculations2(height)
    
