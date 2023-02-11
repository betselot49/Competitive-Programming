class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curSum = sum(nums[:k])
        maxAverage = curSum / k
        left = 0
        right = k
        while right < len(nums):
            curSum += (nums[right] - nums[left])
            maxAverage = max(maxAverage, curSum/k)
            left += 1
            right += 1
            
        return maxAverage
            

            
        