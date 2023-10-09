class Solution:
    def strStr(self, haystack: str, needle: str) -> int:       
        lps = [0]
        i = 0
        j = 1
        while j < len(needle):
            if i == 0 and needle[i] != needle[j]:
                lps.append(0)
                j += 1
            elif needle[i] == needle[j]:
                lps.append(i + 1)
                i += 1
                j += 1
            else:
                i = lps[i - 1]
        
        i = 0
        j = 0
        while i < len(haystack):
            if j == len(needle): return i - len(needle)
            
            elif j == 0 and needle[j] != haystack[i]:
                i += 1
                
            elif needle[j] == haystack[i]:
                i += 1
                j += 1
            else:
                j = lps[j - 1]
        
        if j == len(needle): return i - len(needle)
        return -1

