"""
98. Validate Binary Search Tree

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:
    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

Example 1:

    2
   / \
  1   3
Input: [2,1,3]
Output: true

Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def recursively_all_values(self, root: Optional[TreeNode],
                               prev_left_values: List[int],
                               prev_right_values: List[int],
                               ) -> bool:
        """
        Keep track of right and left values
        for comparing at every new root value
        """
        # base case - empty node
        if not root:
            return True

        # print('root.val = ', root.val)

        # all previous left must be greater than current root
        for val in prev_left_values:
            # print('prev_left_values, val = ', val)
            if root.val >= val:
                return False

                # all previous right must be less than current root
        for val in prev_right_values:
            # print('prev_right_values, val = ', val)
            if root.val <= val:
                return False

        left_check = self.recursively_all_values(
            root.left,
            prev_left_values + [root.val],
            prev_right_values
        )
        right_check = self.recursively_all_values(
            root.right,
            prev_left_values,
            prev_right_values + [root.val]
        )
        # print('right_check = ', right_check)
        # print('left_check = ', left_check)

        return right_check and left_check

    def recursively_last_values(
            self,
            root: Optional[TreeNode],
            min_limit: float,
            max_limit: float
    ) -> bool:
        """
        Keep track only for min and max values
        """
        # base case - empty node
        if not root:
            return True

        if root.val >= max_limit:
            return False

        if root.val <= min_limit:
            return False

        left_check = self.recursively_last_values(
            root.left,
            min_limit,
            root.val
        )
        right_check = self.recursively_last_values(
            root.right,
            root.val,
            max_limit
        )
        # print('right_check = ', right_check)
        # print('left_check = ', left_check)
        return right_check and left_check

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # return self.recursively_all_values(root, [], [])
        return self.recursively_last_values(root, float('-inf'), float('inf'))
