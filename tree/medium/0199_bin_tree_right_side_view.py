"""
199. Binary Tree Right Side View

Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []

"""
from typing import List, Optional
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def bfs_1(self, root: Optional[TreeNode]) -> List[int]:
        """
        BFS + log level of node
        """
        if root is None:
            return []
        queue = [(root, 0)]

        levels = defaultdict(list)
        max_level = -1

        while queue:
            node, level = queue.pop(0)
            if level > max_level:
                max_level = level

            # print('level = ', level)
            # print('node.val = ', node.val)
            levels[level].append(node.val)
            # print('levels = ', levels)
            for next_node in [node.right, node.left]:
                if next_node is not None:
                    queue.append((next_node, level + 1))

        # print('max_level = ', max_level)
        result = []
        for cur_level in range(max_level + 1):
            val = levels[cur_level][0]
            result.append(val)

        return result

    def bfs_2(self, root: Optional[TreeNode]) -> List[int]:
        """
        BFS more compact
        """
        if root is None:
            return []
        queue = [root]
        result = []

        while queue:
            result.append(queue[0].val)
            len_q = len(queue)

            for _ in range(len_q):
                node = queue.pop(0)

                for next_node in [node.right, node.left]:
                    if next_node is not None:
                        queue.append(next_node)

        return result

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # return self.bfs_1(root)  # accepted solution
        return self.bfs_2(root)  # accepted solution
