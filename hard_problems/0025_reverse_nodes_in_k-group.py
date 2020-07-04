"""
25. Reverse Nodes in k-Group

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5
For k = 2, you should return: 2->1->4->3->5
For k = 3, you should return: 3->2->1->4->5

Note:

    Only constant extra memory is allowed.
    You may not alter the values in the list's nodes, only nodes itself may be changed.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    
    def reverseListIteratively(self, 
                               prev_start_node: ListNode, 
                               start_node: ListNode, 
                               next_after_k: ListNode) -> ListNode:
        cur = start_node 
        prev_node = next_after_k
        
        while cur != next_after_k:
            # save next node of current node
            next_node = cur.next
            # change link to previous node
            cur.next = prev_node
            # save previouse node
            prev_node = cur
            # go to next node in usual order
            cur = next_node
        
        # if it is not first reverse
        if prev_start_node is not None:
            prev_start_node.next = prev_node
        
        return prev_node, start_node
    
    def iterativelySeveralReversings(self, head: ListNode, k: int) -> ListNode:
        # Runtime: 60 ms, faster than 24.73% of Python3 online submissions
        # Memory Usage: 14.7 MB, less than 81.41% of Python3 online submissions
        # break the task to k full linked list reverses
        
        first_node = cur_prev_start_node = cur_start_node = k_node = head
        reverses = 0
        
        while k_node is not None:
            
            # go to k-th node
            for _ in range(k-1):
                if k_node.next is not None:
                    k_node = k_node.next
                else:
                    return first_node
            
            # save next element after k (even if it's None)
            next_after_k = k_node.next
            
            if reverses == 0:
                # reverse first part of list
                cur_start_node, cur_prev_start_node = self.reverseListIteratively(
                    None, 
                    cur_start_node,
                    next_after_k)
                # save head of 1st reverse
                first_node = cur_start_node
            else:
                # reverse part of list
                cur_start_node, cur_prev_start_node = self.reverseListIteratively(
                    cur_prev_start_node, 
                    cur_start_node, 
                    next_after_k)
            
            reverses += 1
            
            # go to node after reversed nodes
            cur_start_node = next_after_k
            k_node = next_after_k
            
        return first_node
        
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        return self.iterativelySeveralReversings(head, k)
