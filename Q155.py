"""
Q155
Min Stack
Easy

:stack:

Design a stack that supports push, pop, top, and retrieving the
minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min_ = []

    def push(self, x: int) -> None:
        self.data.append(x)
        if not self.min_:
            self.min_.append(x)
        else:
            self.min_.append(min(self.min_[-1], x))

    def pop(self) -> None:
        self.min_.pop()
        return self.data.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.min_[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()