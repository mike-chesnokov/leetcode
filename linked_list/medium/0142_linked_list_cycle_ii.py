"""
142. Linked List Cycle II

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

Constraints:
    The number of the nodes in the list is in the range [0, 104].
    -105 <= Node.val <= 105
    pos is -1 or a valid index in the linked-list.
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
    
    def findCycleLen(self, head: ListNode) -> int:
        cur_node = head
        steps = 1
        
        while True:
            # other node
            next_node = cur_node
            
            # make 2^k steps from current
            for ind in range(steps):
                if next_node.next is None:
                    return None
                
                next_node = next_node.next
                if next_node == cur_node:
                    return ind + 1
                
            cur_node = next_node
            steps *= 2   
        
    
    def twoPointersCycleLen(self, head: ListNode) -> ListNode:
        # Runtime: 44 ms, faster than 96.04% of Python3 online submissions
        # Memory Usage: 16.7 MB, less than 94.51% of Python3 online submissions
        # 1) find cycle len (using 2^k steps)
        # 2) init 2 pointers: 1st and 2nd; 2nd go to cycle_length node
        
        if head is None:
            return None
        
        cur_node = head
        
        cycle_len = self.findCycleLen(head)
        if cycle_len is None:
            return None
                
        first = second = head
        
        for _ in range(cycle_len):
            second = second.next
        
        while first != second:
            first = first.next
            second = second.next
            
        return first

    def bruteforce(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Simply go through the linked list
        """
        if head is None:
            return None

        all_nodes_set = set()

        while head and head not in all_nodes_set:
            all_nodes_set.add(head)
            head = head.next

        return head

    def detectCycle(self, head: ListNode) -> ListNode:
        return self.twoPointersCycleLen(head)
