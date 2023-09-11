class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        max_art = 1
        dp = defaultdict(int)
       
        for num in arr[::-1]:
            dp[num] = max(dp[num], dp[num+diff] + 1)
            max_art = max(max_art, dp[num])
            
        return max_art