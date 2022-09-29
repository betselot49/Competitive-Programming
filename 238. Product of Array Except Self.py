class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1]
        cur_product = nums[0]
        for i in range(1, n):
            output.append(cur_product)
            cur_product *= nums[i]
        
        cur_product = nums[-1]
        for i in range(n - 2, -1, -1):
            output[i] *= cur_product
            cur_product *= nums[i]
        return output
        
