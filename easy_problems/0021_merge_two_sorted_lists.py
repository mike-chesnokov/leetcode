"""
21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new sorted list.
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # return self.mergeTwoListsIterative(l1, l2)
        return self.mergeTwoListsRecursive(l1, l2)

    def mergeTwoListsRecursive(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Recursive solution"""
        if l1 is None and l2 is None:
            return None
        if l1 is None and l2 is not None:
            return l2
        if l1 is not None and l2 is None:
            return l1

        if l1.val <= l2.val:
            node = self.mergeTwoListsRecursive(l1.next, l2)
            l1.next = node
            return l1
        else:
            node = self.mergeTwoListsRecursive(l1, l2.next)
            l2.next = node
            return l2

    def mergeTwoListsIterative(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Iterative solution"""
        merged_list = cur_node = ListNode(0)

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                cur_node.next = l1
                l1 = l1.next
            else:
                cur_node.next = l2
                l2 = l2.next

            cur_node = cur_node.next

        cur_node.next = l1 or l2

        return merged_list.next
