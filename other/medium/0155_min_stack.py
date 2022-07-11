"""
155. Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
"""


class MinStack:
    """
    Use 2 stacks:
    1) stack with values
    2) stack with current min
    On each appended value store current min value in stack_min
    """
    def __init__(self):
        self.stack = []
        self.stack_mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.stack_mins:
            cur_min = self.stack_mins[-1]
            if val < cur_min:
                self.stack_mins.append(val)
            else:
                self.stack_mins.append(cur_min)
        else:
            self.stack_mins.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.stack_mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
