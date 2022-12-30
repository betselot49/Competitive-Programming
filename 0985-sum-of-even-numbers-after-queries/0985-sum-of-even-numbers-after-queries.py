class Solution:
    def even(self, num):
        if num % 2 == 0:
            return True
        return False
    
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        totalEven = 0
        output = []
        
        for num in nums:
            if self.even(num):
                totalEven += num
                
        for query in queries:
            preValue = nums[query[1]]
            nums[query[1]] += query[0]
            curValue = nums[query[1]]
            
            if self.even(curValue):
                if self.even(preValue):
                    totalEven += curValue - preValue
                else:
                    totalEven += curValue
            else:
                if self.even(preValue):
                    totalEven -= preValue
            
            output.append(totalEven)
            
        return output