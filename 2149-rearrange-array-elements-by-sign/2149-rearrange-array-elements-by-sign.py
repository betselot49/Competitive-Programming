class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        rearranged = []
        for num in nums:
            if num < 0:
                negative.append(num)
            else:
                positive.append(num)
                
        for index in range(len(negative)):
            rearranged.append(positive[index])
            rearranged.append(negative[index])
        
        return rearranged