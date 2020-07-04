"""
783. Minimum Distance Between BST Nodes

Given a Binary Search Tree (BST) with the root node root, 
return the minimum difference between the values of any two different nodes in the tree.

Example :

Input: root = [4,2,6,1,3,null,null]
Output: 1
Explanation:
Note that root is a TreeNode object, not an array.

The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

          4
        /   \
      2      6
     / \    
    1   3  

while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.

Note:
    The size of the BST will be between 2 and 100.
    The BST is always valid, each node's value is an integer, and each node's value is different.
    This question is the same as 530: https://leetcode.com/problems/minimum-absolute-difference-in-bst/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    prev_val = float("-inf")
    min_diff = float("inf")
    stop = False
    
    def minDiffInBSTRecursive(self, cur_node: TreeNode) -> int:
        # In-order traversal for ascending order of values:
        # left -> cur_node -> right
        # also store the previous value
        
        if cur_node is not None and not self.stop:
            # go to left
            self.minDiffInBSTRecursive(cur_node.left)
            
            # compare cur_node
            cur_diff = cur_node.val - self.prev_val
            self.min_diff = min(self.min_diff, cur_diff)
            
            # anyway min diff = 1
            if self.min_diff == 1:
                self.stop = True
                
            self.prev_val = cur_node.val
            
            # go to right
            self.minDiffInBSTRecursive(cur_node.right)
                    
        return self.min_diff
        
        
    def inOrderTraversal(self, root: TreeNode) -> int:
        # Runtime: 56 ms, faster than 5.64% of Python3 online submissions
        # Memory Usage: 13.8 MB, less than 75.70% of Python3 online submissions
        return self.minDiffInBSTRecursive(root)      
                
    def minDiffInBST(self, root: TreeNode) -> int:
        return self.inOrderTraversal(root)
