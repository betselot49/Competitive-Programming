class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums) - 1
        maxJump = nums[0]
        swapIdx = 0
        
        for idx, num in enumerate(nums):
            if idx == N: return True
            
            if maxJump - (idx - swapIdx) <= num:
                maxJump = num
                swapIdx = idx
                
            if maxJump == 0: return False
            