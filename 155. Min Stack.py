class MinStack:

    def __init__(self):
        self.stack = []
        self.min = -1
        self.minStack = [-1]

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.min += 1
            self.minStack.append(self.min)
        else:
            if val < self.stack[self.min]:
                self.min = len(self.stack)
                self.minStack.append(self.min)
        self.stack.append(val)
    
    
    def pop(self) -> None:
        if len(self.stack) > 0:
            pop = self.stack.pop()
            if self.min == len(self.stack):
                self.minStack.pop(-1)
                self.min = self.minStack[-1]
            return pop
            
        
    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]     

    def getMin(self) -> int:
        if len(self.stack) > 0:
            return self.stack[self.min]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
