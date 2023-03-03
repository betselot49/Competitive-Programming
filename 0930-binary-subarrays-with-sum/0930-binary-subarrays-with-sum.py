class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pre_sum = [0]
        for num in nums:
            pre_sum.append(num+pre_sum[-1])
     
        count = defaultdict(int)
        count[0] = 1
        result = 0
        for num in pre_sum[1:]:
            result += count[num-goal]
            count[num] += 1
        return result
 
              
            
        