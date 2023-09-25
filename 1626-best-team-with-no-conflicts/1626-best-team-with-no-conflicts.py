class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        N, dp, max_score = len(ages), {}, 0
        age_score = sorted([(ages[i], scores[i]) for i in range(N)])
        
        for i in range(N):
            local_max = 0
            for j in range(i-1, -1, -1):
                if age_score[i][1] >= age_score[j][1]:
                    local_max = max(local_max, dp[j])
                    
            dp[i] = local_max + age_score[i][1]
            max_score = max(max_score, dp[i])
        
        return max_score
        
        
        
        