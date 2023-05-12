class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        cost_diff = []
        for i in range(1, len(heights)):
            if heights[i] <= heights[i-1]:
                cost_diff.append(0)
            else:
                cost_diff.append(heights[i] - heights[i-1])
                
        heap = []
        heapify(heap)
        curr = 0
        for cost in cost_diff:
            heappush(heap, -cost)
            curr += cost
            if curr > bricks:
                largest = heappop(heap)
                if not ladders: return len(heap)
                heappush(heap, 0)
                ladders -= 1
                curr += largest
        
        return len(heap)