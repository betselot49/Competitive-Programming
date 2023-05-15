class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        N = len(matrix)
        heapify(heap)
        for row in range(N):
            heappush(heap, (matrix[row][0], row, 0))
            
        for _ in range(k):
            popped, row, col = heappop(heap)
            if col + 1 < N:
                heappush(heap, (matrix[row][col+1], row, col+1))
        return popped