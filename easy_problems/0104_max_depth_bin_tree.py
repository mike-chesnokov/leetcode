"""
104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node
down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_depth_recursive(self, root: Optional[TreeNode], cnt) -> int:
        """Recursive solution"""
        if root is None:
            return cnt
        if root.left is None and root.right is None:
            # print(root.val)
            return cnt + 1

        if root.left or root.right:
            left_depth = self.max_depth_recursive(root.left, cnt + 1)
            right_depth = self.max_depth_recursive(root.right, cnt + 1)
            # print(root.val)
            # print(left_depth, right_depth)
            return max(left_depth, right_depth)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.max_depth_recursive(root, 0)
