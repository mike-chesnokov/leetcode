"""
654. Maximum Binary Tree

You are given an integer array nums with no duplicates.
A maximum binary tree can be built recursively from nums using the following algorithm:
    Create a root node whose value is the maximum value in nums.
    Recursively build the left subtree on the subarray prefix to the left of the maximum value.
    Recursively build the right subtree on the subarray suffix to the right of the maximum value.

Return the maximum binary tree built from nums.

Input: nums = [3,2,1,6,0,5]
Output: [6,3,5,null,2,0,null,null,1]
Explanation: The recursive calls are as follow:
- The largest value in [3,2,1,6,0,5] is 6. Left prefix is [3,2,1] and right suffix is [0,5].
    - The largest value in [3,2,1] is 3. Left prefix is [] and right suffix is [2,1].
        - Empty array, so no child.
        - The largest value in [2,1] is 2. Left prefix is [] and right suffix is [1].
            - Empty array, so no child.
            - Only one element, so child is a node with value 1.
    - The largest value in [0,5] is 5. Left prefix is [0] and right suffix is [].
        - Only one element, so child is a node with value 0.
        - Empty array, so no child.

Input: nums = [3,2,1]
Output: [3,null,2,null,1]
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def find_max(self, nums: List[int]):
        max_el = -1
        max_ind = -1
        for ind, el in enumerate(nums):
            if el > max_el:
                max_el = el
                max_ind = ind
        return max_ind, max_el

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        """Recursive solution"""
        if not nums:
            return None

        max_ind, max_el = self.find_max(nums)
        left_nums = nums[:max_ind]
        right_nums = nums[max_ind + 1:]
        root = TreeNode(val=max_el, left=None, right=None)

        if left_nums:
            root.left = self.constructMaximumBinaryTree(left_nums)

        if right_nums:
            root.right = self.constructMaximumBinaryTree(right_nums)

        return root
