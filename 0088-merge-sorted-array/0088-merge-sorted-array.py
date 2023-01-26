class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        index = n + m - 1
        pointer1 = m - 1
        pointer2 = n - 1
        while pointer2 >= 0 and pointer1 >= 0:
            if nums1[pointer1] > nums2[pointer2]:
                nums1[index] = nums1[pointer1]
                pointer1 -= 1
                index -= 1
            else:
                nums1[index] = nums2[pointer2]
                pointer2 -= 1
                index -= 1
        while pointer2 >= 0:
            nums1[index] = nums2[pointer2]
            pointer2 -= 1
            index -= 1
    