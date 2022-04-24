"""
95. Unique Binary Search Trees II

Given an integer n, return all the structurally unique BST's (binary search trees),
which has exactly n nodes of unique values from 1 to n.
Return the answer in any order.

Example 1:
Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

Example 2:
Input: n = 1
Output: [[1]]
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        if n == 1:
            return [TreeNode(1, None, None)]

        return self.generateTreesRecursive(1, n)

    def generateTreesRecursive(self, start: int, end: int) -> List[Optional[TreeNode]]:
        """
        We make each possible left child by cycling through all values less than the current root or [1,curRootVal -1].
        We make each possible right child by cycling through all values greater than the current root or [curRootVal + 1, n]
        """
        if start > end:
            return [None]  # to set cur_root.left = None

        all_trees = []

        for val in range(start, end + 1):
            # cur_root = TreeNode(val)

            # get left subtrees (less than val)
            left_subtrees = self.generateTreesRecursive(start, val - 1)
            # get right subtrees (greater than val)
            right_subtrees = self.generateTreesRecursive(val + 1, end)

            for l_subtree in left_subtrees:
                for r_subtree in right_subtrees:
                    cur_root = TreeNode(val)
                    cur_root.left = l_subtree
                    cur_root.right = r_subtree

                    # cur_root is now the root of a BST
                    all_trees.append(cur_root)

        return all_trees
