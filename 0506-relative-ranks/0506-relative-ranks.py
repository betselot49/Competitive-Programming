class Solution:
    def findRelativeRanks(self, scores: List[int]) -> List[str]:
        dic = {score:idx for idx, score in enumerate(scores)}
        scores.sort(reverse = True)
        
        ans = [""] * len(scores)
        for idx, score in enumerate(scores):
            if idx == 0:
                ans[dic[score]] = "Gold Medal"
            elif idx == 1:
                ans[dic[score]] = "Silver Medal"
            elif idx == 2:
                ans[dic[score]] = "Bronze Medal"
            else:
                ans[dic[score]] = str(idx+1)
        
        return ans
