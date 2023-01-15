"""
328. Odd Even Linked List

Given the head of a singly linked list,
group all the nodes with odd indices together followed by the nodes with even indices,
 and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example 1:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

Constraints:
    The number of nodes in the linked list is in the range [0, 104].
    -106 <= Node.val <= 106
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def bruteforce(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Go through linked list 1 time
        """
        if not head:
            return None

        if not head.next or not head.next.next:
            return head

        cur_node = head
        head2 = next_node = head.next

        while next_node and next_node.next:
            # print('start:',cur_node.val, next_node.val)

            # change next link for cur_node
            cur_node.next = next_node.next
            cur_node = cur_node.next

            # change next link for next_node
            next_node.next = cur_node.next
            next_node = next_node.next

            # print('end:', cur_node, next_node)

        # add even list to the end
        cur_node.next = head2

        return head

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.bruteforce(head)
