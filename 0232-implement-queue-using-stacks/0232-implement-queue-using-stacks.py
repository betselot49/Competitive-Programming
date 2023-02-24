class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue = [x] + self.queue

    def pop(self) -> int:
        if not self.empty():
            return self.queue.pop()
    def peek(self) -> int:
        if not self.empty(): 
            return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()