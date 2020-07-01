"""
92. Reverse Linked List II

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""

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
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None
        
        if m==n:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        cur_node = last_node = head
        if m > 1:
            prev_node = head
        else:
            prev_node = dummy
            
        temp = None
        m_node = None
        ind = 1
        while ind < n + 1:

            if ind < m - 1:
                last_node = last_node.next
                prev_node = prev_node.next
                cur_node = cur_node.next

            if ind == m - 1:
                last_node = last_node.next
                cur_node = cur_node.next

            if ind == m:
                last_node = last_node.next
                next_node = cur_node.next
                m_node = cur_node
                cur_node.next = temp
                temp = cur_node

                cur_node = next_node             

            if ind > m and ind <= n:
                last_node = last_node.next

                next_node = cur_node.next
                cur_node.next = temp
                temp = cur_node

                cur_node = next_node       

            ind += 1
  
        prev_node.next = temp
        m_node.next = last_node

        return dummy.next
