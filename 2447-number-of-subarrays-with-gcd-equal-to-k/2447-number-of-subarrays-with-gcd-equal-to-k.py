class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def gcd(a, b): 
            a, b = min(a, b), max(a, b)
            while a:
                a, b = b % a, a
            return b
                
        sub_arrays = 0
        for left, num in enumerate(nums):
            right = left
            count = 0
            while right < len(nums) and gcd(num, nums[right]) != k:
                if nums[right] % k == 0:
                    right += 1
                else:
                    right = len(nums)
            
            if right == len(nums):
                continue
            
            count += 1
            right += 1
            while right < len(nums) and nums[right] % k == 0:
                right += 1
                count += 1
                
            temp = left - 1
            leftCounter = 1
            while temp >= 0 and nums[temp] and nums[temp] % k == 0:
                temp -= 1
                leftCounter += 1
            
            count *= leftCounter
            nums[left] = 0
            print(num, count)
            sub_arrays += count
        return sub_arrays
    
    """
    [10,19,8,2,12,17]
                     |
     |
    
    
    4
    
    
    """
 
            
          