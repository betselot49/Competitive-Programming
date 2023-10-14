class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0
        sorted = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                sorted.append(nums1[i])
                i += 1
            else:
                sorted.append(nums2[j])
                j += 1
        if j < len(nums2):
            sorted += nums2[j:]
        if i < len(nums1):
            sorted += nums1[i:]
        if len(sorted) % 2 == 0:
            mid = (sorted[len(sorted) // 2] + sorted[(len(sorted) // 2) - 1]) / 2
        else:
            mid = sorted[len(sorted) // 2]
        return mid