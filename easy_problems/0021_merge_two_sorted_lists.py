"""
21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new sorted list.
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        if not l1 or not l2:
            return l1 or l2

        cur_node = None

        if l1.val < l2.val:
            cur_node = l1
            cur_node.next = self.mergeTwoLists(l1.next, l2)
            return cur_node
        else:
            cur_node = l2
            cur_node.next = self.mergeTwoLists(l1, l2.next)
            return cur_node
