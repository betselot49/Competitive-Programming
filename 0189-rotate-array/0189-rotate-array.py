class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
# < ====  reverse the array and rotate before and after k individually. ==== >
 
        k = k % len(nums)
        nums.reverse()
        left, right = 0, k-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        left, right = k, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
