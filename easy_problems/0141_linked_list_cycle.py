"""
141. Linked List Cycle

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.


Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
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
    
    def pow2steps(self, head: ListNode) -> bool:
        # Runtime: 52 ms, faster than 52.67% of Python3 online submissions
        # Memory Usage: 16.8 MB, less than 79.77% of Python3 online submissions
        # make make 2^k steps from current and compare
        # making steps untill cycle length < 2^k
        if head is None:
            return False
        
        cur_node = head
        steps = 1
        
        while True:
            # other node
            next_node = cur_node
            
            # make 2^k steps from current
            for _ in range(steps):
                if next_node.next is None:
                    return False
                
                next_node = next_node.next
                if next_node == cur_node:
                    return True
                
            cur_node = next_node
            steps *= 2
            
        
    def hasCycle(self, head: ListNode) -> bool:
        return self.pow2steps(head)
