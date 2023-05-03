class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)
        k = len(nums) - k
        for _ in range(k):
            heappop(nums)
        return heappop(nums)