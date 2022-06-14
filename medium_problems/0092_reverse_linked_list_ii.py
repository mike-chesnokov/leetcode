"""
92. Reverse Linked List II

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_next_list(self):
        cur_node = self
        while cur_node is not None:
            print(cur_node.val)
            cur_node = cur_node.next


class Solution(object):
    def reverseBetween(self,
                       head: Optional[ListNode],
                       left: int,
                       right: int) -> Optional[ListNode]:
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if not head:
            return None
        
        if left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        cur_node = last_node = head
        if left > 1:
            prev_node = head
        else:
            prev_node = dummy
            
        temp = None
        m_node = None
        ind = 1
        while ind < right + 1:

            if ind < left - 1:
                last_node = last_node.next
                prev_node = prev_node.next
                cur_node = cur_node.next

            if ind == left - 1:
                last_node = last_node.next
                cur_node = cur_node.next

            if ind == left:
                last_node = last_node.next
                next_node = cur_node.next
                m_node = cur_node
                cur_node.next = temp
                temp = cur_node

                cur_node = next_node             

            if left < ind <= right:
                last_node = last_node.next

                next_node = cur_node.next
                cur_node.next = temp
                temp = cur_node

                cur_node = next_node       

            ind += 1
  
        prev_node.next = temp
        m_node.next = last_node

        return dummy.next

    def reverse_list(self, head, stop_n):
        cur_n = head
        prev_n = None

        while cur_n is not stop_n:
            next_n = cur_n.next
            cur_n.next = prev_n
            prev_n = cur_n
            cur_n = next_n

        return prev_n, head

    def reverseBetween2(self,
                       head: Optional[ListNode],
                       left: int,
                       right: int) -> Optional[ListNode]:
        if head is None:
            return None

        if left == right:
            return head

        # go to left ind
        i = 1
        cur_n = head
        first_n = None
        start_reverse_n = None
        # iterate until right
        while i < right + 1:
            if i == left - 1:
                first_n = cur_n
            if i == left:
                start_reverse_n = cur_n
            cur_n = cur_n.next
            i += 1
        last_n = cur_n
        # inverse inner list
        new_start_node, new_end_node = self.reverse_list(start_reverse_n,
                                                         last_n)
        # process case when left == 1
        if first_n is None:
            head = new_start_node
        else:
            first_n.next = new_start_node
        new_end_node.next = last_n

        return head

