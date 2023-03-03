class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        total = 0
        while self.stack and self.stack[-1][0] <= price:
            total += self.stack.pop()[1]
        self.stack.append([price, total + 1])
        return total + 1

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

