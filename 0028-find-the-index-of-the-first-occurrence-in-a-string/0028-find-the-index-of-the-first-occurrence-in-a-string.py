class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        N = len(needle)
        for idx in range(len(haystack) - len(needle) + 1):
            if haystack[idx:idx+N] == needle:
                return idx
        return -1