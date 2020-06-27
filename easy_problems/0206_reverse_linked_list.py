"""
206. Reverse Linked List

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
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

class Solution:
    
    def reverseListRecursevely(self, prev: ListNode, cur: ListNode) -> ListNode:
        # Runtime: 32 ms, faster than 87.46% of Python3 online submissions
        # Memory Usage: 18.7 MB, less than 8.67% of Python3 online submissions
        
        head = cur
        if cur.next != None:
            head = self.reverseListRecursevely(cur, cur.next)
        cur.next = prev
        return head        
    
    def reverseListRecursevely2(self, head: ListNode) -> ListNode:
        # Runtime: 32 ms, faster than 87.46% of Python3 online submissions
        # Memory Usage: 18.4 MB, less than 20.54% of Python3 online submissions
        
        if head.next is None or head is None:
            return head
        else:
            # go to last node
            new_node = self.reverseListRecursevely2(head.next)
            # create reverse link to itself
            head.next.next = head
            # clear usual link
            head.next = None
    
        return new_node
    
    def reverseListIteratively(self, head: ListNode) -> ListNode:
        # Runtime: 36 ms, faster than 68.57% of Python3 online submissions
        # Memory Usage: 15.1 MB, less than 98.11% of Python3 online submissions 
        cur = head 
        prev_node = None
        
        while cur is not None:
            # save next node of current node
            next_node = cur.next
            # change link to previous node
            cur.next = prev_node
            # save previouse node
            prev_node = cur
            # go to next node in usual order
            cur = next_node
        
        return prev_node
    
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        # return self.reverseListRecursevely(None, head)
        # return self.reverseListRecursevely2(head)
        return self.reverseListIteratively(head)
