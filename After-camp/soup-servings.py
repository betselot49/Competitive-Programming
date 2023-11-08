class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 4500: return 1

        @cache
        def dp(n1, n2):
            if n1 <= 0 and n2 > 0: return 1
            if n1 <= 0 and n2 <= 0: return 0.5
            if n2 <= 0: return 0
          
            return 0.25 * (dp(n1-100, n2-0) + dp(n1-75, n2-25) + dp(n1-50, n2-50) + dp(n1-25, n2-75))
        
        return dp(n, n)
        