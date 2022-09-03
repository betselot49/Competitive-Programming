class MyQueue:

    def __init__(self):
        self.stack1 = []        

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        stack2 = []
        while not self.empty():
            stack2.append(self.stack1.pop())
        
        temp = stack2.pop()
        while len(stack2) > 0:
            self.stack1.append(stack2.pop())
        return temp

    def peek(self) -> int:
        stack2 = []
        while not self.empty():
            stack2.append(self.stack1.pop())
        
        temp = stack2[-1]
        while len(stack2) > 0:
            self.stack1.append(stack2.pop())
        return temp
      
    def empty(self) -> bool:
        return len(self.stack1) == 0
   
# OR

class MyQueue:

    def __init__(self):
        self.queue = []        

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if not self.empty():
            temp = self.queue[0]
            self.queue.remove(temp)
            return temp

    def peek(self) -> int:
        if not self.empty():
            return self.queue[0]
      
    def empty(self) -> bool:
        if len(self.queue) == 0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(x)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
