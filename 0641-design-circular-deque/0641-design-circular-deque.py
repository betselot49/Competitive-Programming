class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = [None] * (k+1)
        self.read = 0
        self.write = 0
        self.k = k

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            if self.read == 0:
                self.read = self.k
            else:
                self.read -= 1
            self.deque[self.read] = value
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            self.deque[self.write] = value
            if self.write == self.k:
                self.write = 0
            else:
                self.write += 1
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            self.deque[self.read] = None
            if self.read == self.k:
                self.read = 0
            else:
                self.read += 1
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            if self.write == 0:
                self.write = self.k
            else:
                self.write -= 1
            self.deque[self.write] = None
            return True
        else:
            return False

    def getFront(self) -> int:
        if not self.isEmpty():
            return self.deque[self.read]
        else:
            return -1

    def getRear(self) -> int:
        if not self.isEmpty():
            if self.write == 0:
                return self.deque[self.k]
            else:
                return self.deque[self.write - 1]
        else:
            return -1

    def isEmpty(self) -> bool:
        if self.write == self.read:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.write == self.k and self.read == 0:
            return True
        elif self.write - self.read == -1:
            return True
        else:
            return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()