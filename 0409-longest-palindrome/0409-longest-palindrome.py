class Solution:
    def longestPalindrome(self, s: str) -> int:
        strCounter = Counter(s)
        oddUsed = False
        palinCount = 0
        for value in strCounter.values():
            if not oddUsed and value % 2 != 0:
                palinCount += value
                oddUsed = True
            elif value % 2 != 0:
                palinCount += value - 1
            else:
                palinCount += value
                
        return palinCount