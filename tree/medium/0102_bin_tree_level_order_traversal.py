"""
102. Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def bfs(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        result = []
        queue = [(root, 0)]

        while queue:
            q_len = len(queue)
            # add new level to result
            result.append([])

            for _ in range(q_len):

                node, level = queue.pop(0)
                # add node value to result
                result[level].append(node.val)

                # add neighbors to queue
                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))

        return result

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return self.bfs(root)

