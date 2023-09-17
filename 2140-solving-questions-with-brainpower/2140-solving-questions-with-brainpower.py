class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        N, running_max = len(questions), 0
        for i in range(N-1, -1, -1):
            _next = questions[i+questions[i][1]+1] if i+questions[i][1]+1 < N else 0
            running_max = max(questions[i][0] + _next, running_max)
            questions[i] = running_max
            
        return running_max
        
        