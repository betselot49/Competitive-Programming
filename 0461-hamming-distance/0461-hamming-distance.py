class Solution(object):
    def hammingDistance(self, x, y):
        """
        100
        010
        
        001
        010
        
        """
        
        mask, diff = 1, 0
        while x > 0 or y > 0:
            if x & mask != y & mask:
                diff += 1
            x >>= 1
            y >>= 1
        return diff
        