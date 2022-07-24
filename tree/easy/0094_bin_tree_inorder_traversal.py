"""
94. Binary Tree Inorder Traversal
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Constraints:
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100
"""

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.traversal = []

    def recursion(self, root: Optional[TreeNode]) -> None:
        """
        Recursive solution
        """
        if not root:
            return None
            # print('root.val = ', root.val)

        if root.left:
            # print('root.left.val = ', root.left.val)
            self.recursion(root.left)

        self.traversal.append(root.val)

        if root.right:
            # print('root.right.val = ', root.right.val)
            self.recursion(root.right)

    def iterative(self, root: Optional[TreeNode]) -> List[int]:
        """
        Iterative solution
        """
        if not root:
            return []

        cur = root
        traversal = []
        stack = []

        while cur or stack:

            # iterate to left to max depth
            while cur:
                stack.append(cur)
                cur = cur.left
            # cur = None => pop node from stack
            cur = stack.pop()
            # add current node to traversal
            traversal.append(cur.val)
            # go to right
            cur = cur.right

        return traversal

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # self.recursion(root)  # accepted solution
        # return self.traversal
        return self.iterative(root)  # accepted solution
