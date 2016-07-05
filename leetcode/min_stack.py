"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""
class MinStack:
    def __init__(self):
        self.stack = []
        self.minData = []
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        
        if len(self.minData) == 0 or self.minData[-1] >= x:
            self.minData.append(x)
        
        
    def isEmpty(self):
        return self.stack == []
        

    # @return nothing
    def pop(self):
        if self.isEmpty():
            return None
        else:
            if self.stack[-1] == self.minData[-1]:
                self.minData.pop()
            return self.stack.pop()
        

    # @return an integer
    def top(self):
        if self.isEmpty():
            return None
        else:
            return self.stack[-1]

    # @return an integer
    def getMin(self):
        if self.minData == []:
            return None
        else:
            return self.minData[-1]