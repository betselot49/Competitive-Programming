class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_ans, N = 0, len(values)
        values[-1] = values[-1] - (N - 1)
        
        for i in range(N-2, -1, -1):
            max_ans = max(max_ans, values[i] + i + values[i + 1])
            values[i] = max(values[i + 1], values[i] - i)
            
        return max_ans
            