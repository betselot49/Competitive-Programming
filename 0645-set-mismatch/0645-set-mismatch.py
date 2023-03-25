class Solution(object):
    def findErrorNums(self, nums):
        idx = 0
        while idx < len(nums):
            curr = nums[idx]
            nums[idx], nums[curr-1] = nums[curr-1], nums[idx]
            if idx+1 == nums[idx] or curr == nums[idx]:
                idx += 1
        
        ans = []
        for idx, num in enumerate(nums):
            if idx+1 != num:
                return [num, idx+1]
                
    