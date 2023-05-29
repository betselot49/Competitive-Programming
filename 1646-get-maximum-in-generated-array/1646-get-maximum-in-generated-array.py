class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n <= 1:
            return n
        nums = [0] * (n + 1)
        nums[0] = 0
        nums[1] = 1
        max_val = 0
        for i in range(2,n+1):
            idx = i // 2
            if i % 2 == 0:
                nums[i] = nums[idx]
            else:
                nums[i] = nums[idx] + nums[idx + 1]
            max_val = max(max_val, nums[i])
            
            
        return max_val
