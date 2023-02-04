class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen = 0
        subString = ''
        for i in range(len(s)):
            left = i 
            while i < len(s) and s[left] == s[i]:
                i += 1
            right = i-1
            
            while left > -1 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            left += 1
            right -= 1
            
            if right - left + 1 > maxLen:
                subString = s[left : right + 1]
                maxLen = len(subString)
                
        return subString
            
            