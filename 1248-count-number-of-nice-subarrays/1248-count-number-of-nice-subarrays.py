class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = right = oddCount = counter = 0
        while right < len(nums):
            if nums[right] % 2 != 0:
                oddCount += 1
                
            tempRight = right
            right += 1
            while oddCount >= k and right < len(nums) and nums[right] %2 == 0:
                right += 1
                
            while oddCount >= k:
                counter += right - tempRight
                if nums[left] %2 != 0:
                    oddCount -= 1
                left += 1
                
        return counter