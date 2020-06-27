"""
24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""

class ListNode(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None

    def print_next_list(self):
        cur_node = self
        while cur_node is not None:
            print(cur_node.val)
            cur_node = cur_node.next
            
            
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
    
        second = head.next
        head.next = self.swapPairs(second.next)
        second.next = head

        return second
