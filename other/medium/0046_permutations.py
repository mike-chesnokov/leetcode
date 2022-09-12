"""
46. Permutations

Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

Constraints:
    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    All the integers of nums are unique.
"""
from typing import List, Set


class Solution:

    def __init__(self):
        self.result = []

    def backtrack(self, nums: List[int], cur_nums: List[int], visited: Set[int]) -> None:
        # base case
        if len(cur_nums) == len(nums):
            self.result.append(cur_nums.copy())
            return

        # iterate over all nums
        for num in nums:
            if num in visited:
                continue
            else:
                # add new num
                cur_nums.append(num)
                visited.add(num)
                # go to the next num
                self.backtrack(nums, cur_nums, visited)
                # backtrack
                cur_nums.pop()
                visited.remove(num)
        return

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums, [], set())
        return self.result
