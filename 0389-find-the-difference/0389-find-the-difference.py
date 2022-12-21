class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = Counter(s)
        t = Counter(t)
        for char in t:
            if char not in s or s[char] < t[char]:
                return char
        