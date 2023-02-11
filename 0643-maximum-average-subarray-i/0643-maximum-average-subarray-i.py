class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curSum = sum(nums[:k])
        maxAverage = curSum / k
        for pointer in range(len(nums)-k):
            curSum += (nums[pointer+k] - nums[pointer])
            maxAverage = max(maxAverage, curSum/k) 
        return maxAverage
            

            
        