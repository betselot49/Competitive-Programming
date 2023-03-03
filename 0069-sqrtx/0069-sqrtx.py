class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        low = 0
        high = x
        while high - low > 1:
            mid = low + (high - low) // 2
            if mid ** 2 > x:
                high = mid
            elif mid ** 2 < x:
                low = mid
            else:
                return mid
        return low