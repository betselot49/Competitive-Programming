class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        N = len(s)
        dp = {N: 0}
        dic = set(dictionary)
        for outer in range(N-1, -1, -1):
            curr = s[outer]
            count = N - outer
            for inner in range(outer+1, N+1):
                result = 0 if curr in dic else len(curr)
                result += dp[inner]
                count = min(count, result)
                if inner < N:
                    curr += s[inner]
                
            dp[outer] = count
        return dp[0]