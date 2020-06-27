"""
707. Design Linked List

Design your implementation of the linked list. 
You can choose to use the singly linked list or the doubly linked list. 
A node in a singly linked list should have two attributes: val and next. 
val is the value of the current node, and next is a pointer/reference to the next node. 
If you want to use the doubly linked list, 
you will need one more attribute prev to indicate the previous node in the linked list. 
Assume all nodes in the linked list are 0-indexed.

Implement these functions in your linked list class:

    get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
    addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
    addAtTail(val) : Append a node of value val to the last element of the linked list.
    addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
    deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.

Example:

Input: 
["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
[[],[1],[3],[1,2],[1],[1],[1]]
Output:  
[null,null,null,null,2,null,3]

Explanation:
MyLinkedList linkedList = new MyLinkedList(); // Initialize empty LinkedList
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
linkedList.get(1);            // returns 2
linkedList.deleteAtIndex(1);  // now the linked list is 1->3
linkedList.get(1);            // returns 3
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    # Runtime: 264 ms, faster than 58.89% of Python3 online submissions
    # Memory Usage: 14.2 MB, less than 83.77% of Python3 online submissions
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. 
        If the index is invalid, return -1.
        """
        if index >= self.size:
            return -1
        cur = self.head
        
        # move to index node
        for ind in range(index):
            cur = cur.next
        
        return cur.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. 
        After the insertion, the new node will be the first node of the linked list.
        """
        new_head = ListNode(val)
        new_head.next = self.head
        self.head = new_head
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_tail = ListNode(val)
        cur = self.head
        
        # move to tail node
        for ind in range(self.size - 1):
            cur = cur.next
        
        cur.next = new_tail
        
        self.size += 1
        
    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. 
        If index equals to the length of linked list, the node will be appended to the end of linked list. 
        If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            return
        if index > 0 and index == self.size:
            self.addAtTail(val)
            return
        if index == 0:
            self.addAtHead(val)
            return
        
        # if index < self.size
        new_node = ListNode(val)
        cur = self.head
        
        # move to index - 1 node
        for ind in range(index-1):
            cur = cur.next  
        
        new_node.next = cur.next
        cur.next = new_node 
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
            return
            
        cur = self.head
        # move to index - 1 node
        for ind in range(index-1):
            cur = cur.next    
            
        # if cur is not tail node
        if cur.next is not None:
            cur.next = cur.next.next
        else:
            cur = None
            
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

# ["MyLinkedList","addAtHead","deleteAtIndex"]
# [[],[1],[0]]

# ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
# [[],[1],[3],[1,2],[1],[1],[1]]

# ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
# [[],[1],[3],[1,2],[1],[0],[0]]

# ["MyLinkedList","addAtIndex","addAtIndex","addAtIndex","get"]
# [[],[0,10],[0,20],[1,30],[0]]
