class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        flag = False
        
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
            
        return False