class MyCircularQueue:

    def __init__(self, k: int):
        self.front = 0
        self.rear = 0
        self.k = k
        self.cir_queue = [-1] * self.k
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.cir_queue[self.front] = value
        self.front += 1
        self.front %= self.k
        return True

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.cir_queue[self.rear] = -1
            self.rear += 1
            self.rear %= self.k
            return True
        return False

    def Front(self) -> int:
        return self.cir_queue[self.rear]

    def Rear(self) -> int:
        return self.cir_queue[self.front-1]

    def isEmpty(self) -> bool:
        if self.rear == self.front and self.cir_queue[self.rear] == -1:
            return True
        return False

    def isFull(self) -> bool:
        if self.rear == self.front and self.cir_queue[self.rear] != -1:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()