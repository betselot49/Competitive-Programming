class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        index_map = {num:index for index, num in enumerate(nums2)}
        next_great = [-1] * len(nums2)
        monStack = [nums2[-1]]
        right = len(nums2) - 2
        output = []
        while right >= 0:
            while monStack and monStack[-1] <= nums2[right]:
                monStack.pop()
                
            next_great[right] = monStack[-1] if monStack else -1
            monStack.append(nums2[right])
            right -= 1
        
        for num in nums1:
            output.append(next_great[index_map[num]])
        return output
       
        