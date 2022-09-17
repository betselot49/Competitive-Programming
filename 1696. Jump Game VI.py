class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        length = len(nums)
        heap = [(-nums[0], 0)]
        for i in range(1, length):
            while heap[0][1] < i - k:
                heappop(heap)
            maximum = heap[0][0]
            heappush(heap, (maximum - nums[i], i))
            if i == length - 1:
                return -(maximum - nums[i])
        return nums[0]
