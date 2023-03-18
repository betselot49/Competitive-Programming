class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1: return str(0)
        if k == (2**n) // 2: return str(1)
        if k > (2**n) // 2: return str(1 - int(self.findKthBit(n-1, 2**n - k)))
        return str(self.findKthBit(n-1, k))