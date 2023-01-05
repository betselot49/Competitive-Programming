class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive, negative, rearranged = [], [], []
     
        for num in nums:
            if num < 0:
                negative.append(num)
            else:
                positive.append(num)
                
        for index in range(len(negative)):
            rearranged.append(positive[index])
            rearranged.append(negative[index])
        
        return rearranged
    
    

#  < ==============  reduced space   =================== >    
    
#         negative, positive, rearranged = 0, 0, []
        
#         while positive < len(nums) or negative < len(nums):
#             while positive < len(nums):
#                 if nums[positive] > 0:
#                     rearranged.append(nums[positive])
#                     positive += 1
#                     break
#                 positive += 1
                
#             while negative < len(nums):
#                 if nums[negative] < 0:
#                     rearranged.append(nums[negative])
#                     negative += 1
#                     break
#                 negative += 1
                
#         return rearranged
            
            
        
        
        
        
    
    

    
    
