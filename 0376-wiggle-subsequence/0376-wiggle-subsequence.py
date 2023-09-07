class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        N = len(nums)
        max_wiggle, dp = 1, { N-1 : (1, 1) }
        for i in range(N-2, -1, -1):
            pos = neg = 1
            for j in range(i+1, N):
                if nums[i] < nums[j]:
                    pos = max(pos, dp[j][1] + 1)
                elif nums[i] > nums[j]:
                    neg = max(neg, dp[j][0] + 1)
                    
            dp[i] = (pos, neg)
            max_wiggle = max(max_wiggle, pos, neg)
            
        return max_wiggle
            
            
                    