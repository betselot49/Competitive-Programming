class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for ind in range(len(s)):
            if count[s[ind]] == 1: return ind
        return -1