"""
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
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
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        new_list = cur_node = ListNode(0)
        overflow = 0

        while l1 is not None or l2 is not None:
            val1, val2 = 0, 0
            
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next

            result = val1 + val2 + overflow

            if result > 9:
                cur_node.next = ListNode(result - 10)
                overflow = 1

            elif result <= 9:
                cur_node.next = ListNode(result)
                overflow = 0

            cur_node = cur_node.next  

        if overflow == 1:
            cur_node.next = ListNode(1)
        return new_list.next 
