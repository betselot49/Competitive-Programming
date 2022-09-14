class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = [-1] * len(nums1)
        for i in range(0, len(nums1)):
            j = nums2.index(nums1[i]) + 1
            while j < len(nums2):
                if nums1[i] < nums2[j]:
                    output[i] = nums2[j]
                    break
                j += 1
        return output
        
