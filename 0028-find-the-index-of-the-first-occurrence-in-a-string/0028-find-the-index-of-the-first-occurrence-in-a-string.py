class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        for i in range(len(haystack) - m + 1):
            temp = i
            flag = True
            for j in range(m):
                if haystack[temp] != needle[j]:
                    flag = False
                    break
                temp += 1
            if flag: return i
        return -1