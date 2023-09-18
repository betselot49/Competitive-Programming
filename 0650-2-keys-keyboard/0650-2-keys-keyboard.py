class Solution:
    def minSteps(self, n: int) -> int:
        self.total = 0
        def primeFactor(base, num):
            if num == 1: return self.total
            
            for i in range(base, int(num ** 0.5) + 1):
                if num % i == 0:
                    self.total += i
                    return primeFactor(2, num//i)
                    
            self.total += num
            return primeFactor(num, 1)
        
        return primeFactor(2, n)

                    
            