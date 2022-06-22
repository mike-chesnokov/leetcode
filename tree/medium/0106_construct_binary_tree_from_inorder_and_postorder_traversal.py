"""
106. Construct Binary Tree from Inorder and Postorder Traversal

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def BSTStack(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # Runtime: 60 ms, faster than 81.57% of Python3 online submissions
        # Memory Usage: 17.4 MB, less than 98.14% of Python3 online submissions
        if not inorder:
            return None
        
        # inorder transform to BST of indexes
        value_to_index = {el:ind for ind, el in enumerate(inorder)}
        
        # feature of postorder
        root = TreeNode(postorder[-1])
        
        # (node, min_index), below node all indexes are greater than min_index
        # None == -oo
        stack = [(root, None)]
        
        # go through postorder from end
        for val in reversed(postorder[:-1]):
            # print(stack)
            new_node = TreeNode(val)
            new_node_index = value_to_index[val]
            
            # get node and min_index from stack
            cur_node, min_index = stack[-1]
            cur_node_index = value_to_index[cur_node.val]
            
            # 2 cases
            if new_node_index > cur_node_index:
                cur_node.right = new_node
                stack.append((new_node, cur_node_index))
            else:
                while stack[-1][1] is not None and new_node_index < stack[-1][1]:
                    stack.pop()
                    
                cur_node, min_index = stack[-1]
                cur_node.left = new_node
                stack.append((new_node, min_index))
        
        return root
    
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self.BSTStack(inorder, postorder)
