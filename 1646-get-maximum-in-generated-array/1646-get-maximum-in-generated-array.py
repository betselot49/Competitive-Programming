class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n <= 1: return n
        self.max = 0
        memo = [0, 1]
        for i in range(2, n+1):
            if i % 2 == 0:
                curr = memo[i // 2]
            else:
                curr = memo[i // 2] + memo[i // 2 + 1]
            self.max = max(self.max, curr)
            memo.append(curr)      
        return self.max