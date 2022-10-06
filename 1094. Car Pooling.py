class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x : x[1])
        minHeap = []
        curr_passengers = 0
        for trip in trips:
            
            curr_passengers += trip[0]
            
            while minHeap and minHeap[0][0] <= trip[1]:      # while end in heap <= start in cur_trip
                drop = heapq.heappop(minHeap)[1]
                curr_passengers -= drop
            
            heapq.heappush(minHeap, [trip[2], trip[0]])
                
            if curr_passengers > capacity:
                return False
        
        return True
        
        
