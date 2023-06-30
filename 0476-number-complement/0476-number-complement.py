class Solution(object):
    def findComplement(self, num):
        mask, limit = 1, num
        while mask <= limit:
            num ^= mask
            mask <<= 1
        return num
            