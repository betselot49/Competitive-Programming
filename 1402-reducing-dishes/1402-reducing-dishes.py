class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        N, max_score = len(satisfaction), 0
        for i in range(N, 0, -1):
            curr, total, j = i, 0, N - 1
            while curr > 0:
                total += curr * satisfaction[j]
                j -= 1
                curr -= 1
            max_score = max(max_score, total)
            
        return max_score