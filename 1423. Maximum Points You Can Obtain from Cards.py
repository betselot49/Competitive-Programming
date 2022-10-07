class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:       
        total = sum(cardPoints)
        i = 0
        j = len(cardPoints) - k
        cur_sum = sum(cardPoints[:j])
        max_sum = total - cur_sum
        
        while j < len(cardPoints):
            cur_sum += cardPoints[j]
            cur_sum -= cardPoints[i]
            i += 1
            j += 1
            max_sum = max(max_sum, total - cur_sum)
        return max_sum
    
    
