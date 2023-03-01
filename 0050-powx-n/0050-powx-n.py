class Solution:
    def __init__(self):
        self.cache = {}
        
    def power(self, x, n):
        if n == 0:
            return 1
        
        if n in self.cache:
            return self.cache[n]
        if n % 2 == 0:
            power1 = self.power(x, n // 2)
            power2 = self.power(x, n // 2) 
            
            self.cache[n] = power1 * power2
            return self.cache[n]
        else:
            power = self.power(x, n-1) 
            self.cache[n] = x * power
            
            return self.cache[n] 
    
    
    def myPow(self, x: float, n: int) -> float:
        power = self.power(x, abs(n))
        return power if n > 0 else 1/power