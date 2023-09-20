class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s) - 1
        @cache
        def explore(left, right):
            if left > right: return 0
            if left == right: return 1
            if s[left] == s[right]: return 2 + explore(left+1, right-1)
            else: return max(explore(left+1, right), explore(left, right-1))
        
        return explore(0, N)
            