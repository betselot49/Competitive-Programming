class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        turn  = n & 1
        while n > 0:
            if turn != n & 1: return False
            turn = 1 - turn
            n >>= 1
        return True