class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1
        while right >= 0 and nums[right] == val:
            right -= 1
        while left < right:
            if nums[left] == val:
                nums[left] = nums[right]
                right -= 1
                while right >= 0 and nums[right] == val:
                    right -= 1
            left += 1
        return len(nums) - (len(nums) - right) + 1
    
    
    
 