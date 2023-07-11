class Solution:
    def singleNumber(self, nums):
        negative = 0
        maxi = 0
        for num in nums:
            maxi = max(maxi, abs(num))
            if num < 0:
                negative += 1
        mask = 1
        answer = 0
        
        while mask <= maxi:
            count = 0
            for num in nums:
                if abs(num) & mask == mask:
                    count += 1
            
            if count % 3 != 0:
                answer += mask
            mask <<= 1
            
        
        
        return answer if negative % 3 == 0 else -answer