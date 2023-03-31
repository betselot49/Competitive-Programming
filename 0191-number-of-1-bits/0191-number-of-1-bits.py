class Solution(object):
    def hammingWeight(self, n):
        mask, count = 1, 0
        while n > 0:
            count += mask & n
            n >>= 1
        return count