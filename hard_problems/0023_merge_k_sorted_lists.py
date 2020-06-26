"""
23. Merge k Sorted Lists
Merge k sorted linked lists and return it as one sorted list. 
Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
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
    
    def mergeKListsBruteForse(self, lists: List[ListNode]) -> ListNode:
        # Runtime: 92 ms, faster than 97.97% of Python3 online submissions
        # Memory Usage: 18.1 MB, less than 23.92% of Python3 online submissions
        # simply go through all linked lists
        values = []
        for linked_list in lists:
            while linked_list is not None:
                values.append(linked_list.val)
                linked_list = linked_list.next
        
        # sorting all values
        values_sorted = sorted(values)
        
        # create new linked list and head pointer
        new_linked_list = head = ListNode(0)
        
        for val in values_sorted:
            new_linked_list.next = ListNode(val)
            new_linked_list = new_linked_list.next
            
        return head.next
    
    def mergeKListsSequental(self, lists: List[ListNode]) -> ListNode:
        # Runtime: 4648 ms, faster than 8.33% of Python3 online submissions
        # Memory Usage: 18.1 MB, less than 19.02% of Python3 online submissions
        # set pointers to all heads of lists 
        # and iterate sequentaly through pointers
        pointers = {}
        for list_ind, linked_list in enumerate(lists):
            if linked_list is not None:
                pointers[list_ind] = linked_list
            
        new_linked_list = head = ListNode(0)
        
        # until all pointers are droped
        while len(pointers) > 0:
            # find min val among all nodes
            cur_min_ind = -1
            cur_min = 10e6
            
            for list_ind in pointers:
                cur_val = pointers[list_ind].val
                if cur_val < cur_min:
                    cur_min = cur_val
                    cur_min_ind = list_ind
            
            # create new node of result linked list
            new_linked_list.next = ListNode(cur_min)
            new_linked_list = new_linked_list.next
            
            # go to next node in linked list with min val
            # or drop this linked list from pointers
            if pointers[cur_min_ind].next is not None:
                pointers[cur_min_ind] = pointers[cur_min_ind].next
            else:
                pointers.pop(cur_min_ind, None)
        
        return head.next
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # return self.mergeKListsBruteForse(lists)
        return self.mergeKListsSequental(lists)
