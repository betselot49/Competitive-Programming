class Solution:
    def longestSubarray(self, nums: List[int]) -> int:       
        i, j, maxLen, delCount = 0, 0, 0, 1
    
        while j < len(nums):
            if nums[j]:
                pass
            elif not nums[j] and delCount:
                delCount -= 1
            else:
                maxLen = max(maxLen, j - i - 1)
                while nums[i]:
                    i += 1
                i += 1
            j += 1
        
        return max(maxLen, j - i - 1)
            
            
