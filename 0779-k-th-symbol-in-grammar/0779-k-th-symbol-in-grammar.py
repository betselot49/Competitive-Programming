class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return self.grammer(n, k)   
        
    def grammer(self, num, k):
        if num == 1: return 0
        
        if k % 2 == 0: 
            return 1 - self.grammer(num-1, k // 2) 
        return self.grammer(num-1, (k // 2) + 1)
    
    