class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()   
        N, count =  len(nums), 0
        
        for curr in range(N - 1, 1, -1):
            left, right = 0, curr - 1
            while left < right:
                if nums[left] + nums[right] > nums[curr]:
                    count += right - left
                    right -= 1
                else:
                    left += 1
                    
        return count
                    