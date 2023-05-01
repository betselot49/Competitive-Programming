class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 0
        minus = 1
        while n >= minus:
            n -= minus
            minus += 1
            count += 1
        return count
        
        