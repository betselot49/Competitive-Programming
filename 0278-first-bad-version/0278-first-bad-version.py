# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
#         r = n-1
#         l = 0
#         while(l<=r):
#             mid = l + (r-l)//2
#             if isBadVersion(mid)==False:
#                 l = mid+1
#             else:
#                 r = mid-1
#         return l
    
    
    
        low = 0
        high = n+1
        while low + 1 < high:
            mid = low + (high - low) // 2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid
        return high