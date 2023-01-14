"""
1110. Delete Nodes And Return Forest

Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.

Example 1:
Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]

Example 2:
Input: root = [1,2,4,null,3], to_delete = [3]
Output: [[1,2,4]]

Constraints:

    The number of nodes in the given tree is at most 1000.
    Each node has a distinct value between 1 and 1000.
    to_delete.length <= 1000
    to_delete contains distinct values between 1 and 1000.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def bfs(self, root: Optional[TreeNode], to_delete: Set[int]) -> List[TreeNode]:

        queue = [(root, False)]  # store (Node, has_parent)
        result = []

        while queue:
            cur_node, has_parent = queue.pop(0)

            # process root
            # if node doesn't have a parent and
            # not need to be deleted - it is the root to add
            if cur_node.val not in to_delete and not has_parent:
                result.append(cur_node)

            # define has_parent for left and right nodes
            if cur_node.val in to_delete:
                has_parent = False
            else:
                has_parent = True

            # process left node
            if cur_node.left:
                queue.append((cur_node.left, has_parent))
                if cur_node.left.val in to_delete:
                    # delete node
                    cur_node.left = None

                    # process right node
            if cur_node.right:
                queue.append((cur_node.right, has_parent))
                if cur_node.right.val in to_delete:
                    # delete node
                    cur_node.right = None

        return result

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        if not root:
            return []

        return self.bfs(root, set(to_delete))
