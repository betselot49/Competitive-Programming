class Solution:
    def longestPrefix(self, s: str) -> str:
        lps, left, right = [0 for _ in range(len(s))], 0, 1
        while right < len(s):
            if s[left] == s[right]:
                lps[right] = left + 1
                left += 1
                right += 1
            elif left == 0:
                right += 1
            else:
                left = lps[left - 1]
            
        return s[:lps[-1]]