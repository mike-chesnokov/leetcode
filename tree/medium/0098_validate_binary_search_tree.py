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

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def isValidBSTRecursive(self, node, left_val, right_val):
        # Runtime: 44 ms, faster than 75.87% of Python3 online submissions
        # Memory Usage: 15.9 MB, less than 96.39% of Python3 online submissions
        # recursive walk through tree and check values
        if node is None:
            return True
        
        # left_val < node.val < right_val
        if left_val is not None and left_val >= node.val:
            return False
        if right_val is not None and right_val <= node.val:
            return False
        
        return self.isValidBSTRecursive(node.left, left_val, node.val) \
            and self.isValidBSTRecursive(node.right, node.val, right_val)
    
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidBSTRecursive(root, None, None)
