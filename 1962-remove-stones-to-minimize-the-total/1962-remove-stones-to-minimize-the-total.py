class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-i for i in piles]
        heapify(heap)
        for _ in range(k):
            popped = -heappop(heap)
            popped -= popped // 2
            heappush(heap, -popped)
        return -sum(heap)