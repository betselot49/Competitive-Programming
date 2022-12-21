class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        perimeter = 0
        nums.sort()
        for i in range(len(nums)-2, 0, -1):
            twoSum = nums[i] + nums[i-1]
            for j in range(len(nums)-1, i, -1):
                if twoSum > nums[j]:
                    perimeter = twoSum + nums[j]
                    break
            if perimeter:
                break
        return perimeter