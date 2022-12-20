class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        index = n + m - 1
        i = m - 1
        j = n - 1
        while j >= 0 and i >= 0:
            if nums1[i] > nums2[j]:
                nums1[index] = nums1[i]
                i -= 1
                index -= 1
            else:
                nums1[index] = nums2[j]
                j -= 1
                index -= 1
        while j >= 0:
            nums1[index] = nums2[j]
            j -= 1
            index -= 1
    