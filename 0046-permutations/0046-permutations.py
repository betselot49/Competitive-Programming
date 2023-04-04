# Using bit manipulation (turnign on or of the bit (idx) we already used) => instead of set using bit saves space (O(1)) 
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.bit = 0
        self.permutation = []
        def helper(N, nums, path):
            if len(path) == len(nums):
                self.permutation.append(path)
                return
            
            for idx, num in enumerate(nums):
                if 2**(N-idx) & self.bit == 0:
                    path.append(num)
                    self.bit += 2 ** (N - idx)
                    helper(N, nums, path[:])
                    path.pop()
                    self.bit -= 2 ** (N - idx)
        
        helper(len(nums)-1, nums, [])
        return self.permutation

# Using set to avoid using numbers we already used. 

# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         self.seen = set()
#         self.permutation = []
#         def helper(nums, path):
#             if len(path) == len(nums):
#                 self.permutation.append(path)
#                 return
            
#             for num in nums:
#                 if num not in self.seen:
#                     path.append(num)
#                     self.seen.add(num)
#                     helper(nums, path[:])
#                     path.pop()
#                     self.seen.remove(num)
        
#         helper(nums, [])
#         return self.permutation
    
    