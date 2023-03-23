class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = left = 0    
        for right, num in enumerate(nums): 
            if num == 0:
                count += right - left + 1
            else:
                left = right + 1  
        return count
            