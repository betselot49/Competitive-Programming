class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        swap = True
        while swap:
            swap = False
            for i in range(1, len(nums)-1):
                if (nums[i-1] + nums[i+1]) / 2 == nums[i]:
                    nums[i-1], nums[i] = nums[i], nums[i-1]
                    swap = True
        return nums
