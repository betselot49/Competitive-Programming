class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:                
        sub_arrays = 0
        for left, num in enumerate(nums):
            right = left
            count = 0
            # find two numbers that satisfy the condition but the numbers between them are divisble by k
            while right < len(nums) and math.gcd(num, nums[right]) != k: 
                if nums[right] % k == 0:
                    right += 1
                else:
                    right = len(nums)
            
            # if there are no such two numbers fulfilling the condition => continue
            if right == len(nums):
                continue
            
            count += 1
            right += 1
            # open our window to the right until we get number not divisible by k or right being out of bound
            while right < len(nums) and nums[right] % k == 0:
                right += 1
                count += 1
             
            
            # open window to the left until we get number not divisible by k or left being out of bound 
            temp = left - 1
            leftCounter = 1
            while temp >= 0 and nums[temp] and nums[temp] % k == 0:
                temp -= 1
                leftCounter += 1
            
            # calculate total subarrays that can be formed left window length * right window length
            count *= leftCounter
            nums[left] = 0
            sub_arrays += count
            
        return sub_arrays
    
 
            
          
