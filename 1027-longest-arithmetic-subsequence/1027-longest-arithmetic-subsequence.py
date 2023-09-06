class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp, N, max_art = {}, len(nums), 2
        
        for i in range(N-2, -1, -1):
            for j in range(i + 1, N):
                diff = nums[i] - nums[j]
                curr_max = dp.setdefault((j, diff), 1) + 1
                max_art = max(max_art, curr_max)
                if (i, diff) not in dp:
                    dp[(i, diff)] = curr_max
             
        return max_art
                
                
        