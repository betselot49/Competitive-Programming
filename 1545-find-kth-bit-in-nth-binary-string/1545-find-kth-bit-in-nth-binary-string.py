class Solution:
    def binaryStr(self, n):
        if n == 1:
            return "0"
        
        s = self.binaryStr(n-1)
        sPrime = []
        for ind, num in enumerate(s[::-1]):
            sPrime.append("1") if num == "0" else sPrime.append("0")
    
        return s + "1" + "".join(sPrime)
        
    
    def findKthBit(self, n: int, k: int) -> str:
        return self.binaryStr(n)[k-1]

    