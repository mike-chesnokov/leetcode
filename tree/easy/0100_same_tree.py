"""
100. Same Tree
Given the roots of two binary trees p and q, write a function to check
if they are the same or not.
Two binary trees are considered the same if they are structurally identical,
and the nodes have the same value.

Examples:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Input: p = [1,2], q = [1,null,2]
Output: false

Input: p = [1,2,1], q = [1,1,2]
Output: false
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def recursion(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Recursive solution
        """
        # process case p and q = None
        if p is None and q is None:
            return True

        # process case p of q = None
        if p is not None and q is None:
            return False
        if p is None and q is not None:
            return False

        # process case p != q
        if p.val != q.val:
            return False

        # go recursively to next nodes
        left_res = self.recursion(p.left, q.left)
        right_res = self.recursion(p.right, q.right)

        return left_res and right_res

    def are_equal(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # process case p of q = None
        if p is not None and q is None:
            return False
        if p is None and q is not None:
            return False

        # process case p != q
        if p.val != q.val:
            return False

        return True

    def iteration(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Iterative solution
        """
        queue = [(p, q)]

        while queue:

            p_, q_ = queue.pop(0)

            if not p_ and not q_:
                continue

            if not self.are_equal(p_, q_):
                return False
            else:
                queue.append((p_.left, q_.left))
                queue.append((p_.right, q_.right))
        return True

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # return self.recursion(p, q)  # Accepted
        return self.iteration(p, q)  # Accepted
