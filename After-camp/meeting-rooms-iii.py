class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        heapq = []
        heapify(heapq)
        
        free_rooms = [i for i in range(n)]
        heapify(free_rooms)
        
        rooms = defaultdict(int)
        meetings.sort(key=lambda x: x[0])
    
        for start, end in meetings:
            while heapq:
                endTime, index = heappop(heapq)
                if start >= endTime:
                    heappush(free_rooms, index)
                else:
                    heappush(heapq, (endTime, index))
                    break
                    
            if free_rooms:
                index = heappop(free_rooms)
                heappush(heapq, (end, index))
            else:
                endTime, index = heappop(heapq)
                heappush(heapq, (endTime + (end - start), index))
                
            rooms[index] += 1
                
        # Return the first room used most 
        max_used = 0
        most_used = 0
        for index, used in list(rooms.items()):
            if used > max_used:
                max_used = used
                most_used = index
                
        return most_used