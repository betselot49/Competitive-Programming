class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mini = min(nums)
        maxi = max(nums)
        for num in range(mini, 0, -1):
            if mini % num == maxi % num == 0: return num
            
            
#         or 
#         a, b = min(nums), max(nums)
#         while a:
#             a, b = b % a, a
#         return b
        