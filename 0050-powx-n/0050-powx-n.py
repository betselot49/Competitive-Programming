class Solution:
    def __init__(self):
        self.cache = {0 : 1}
      
    def power(self, x, n):
        if n in self.cache: return self.cache[n]

        if n == 1: return x
        
        power = self.power(x, n//2)
        power *= power
        
        return power if n % 2 == 0 else power * x
    
    
    def myPow(self, x: float, n: int) -> float:
        power = self.power(x, abs(n))
        return power if n > 0 else 1/power