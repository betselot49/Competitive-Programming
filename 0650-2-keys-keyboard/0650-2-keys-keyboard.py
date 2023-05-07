class Solution:
    def minSteps(self, n: int) -> int:
        self.count = 0
        def primeFactor(init, n):
            if n == 1: return self.count
            for i in range(init, (n // 2) + 1):
                if n % i == 0:
                    n //= i
                    self.count += i
                    return primeFactor(i, n)
            self.count += n
            return primeFactor(n, 1)
                           
        return primeFactor(2, n)