class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses = sorted(list(set(houses)))
        heaters = sorted(list(set(heaters)))
        index_map = {num : i for i, num in enumerate(houses)}
        
        def binarySearch(target):
            left = -1
            right = len(houses)
            
            while left + 1 < right:
                mid = (left + right) // 2
                if houses[mid] <= target:
                    left = mid
                else:
                    right = mid
            
            return left
        
        min_heap = []
        min_radius = defaultdict(lambda : float("inf"))
        
        for num in heaters:
            left = binarySearch(num)
            if 0 <= left < len(houses):
                curr = houses[left]
                min_radius[curr] = min(min_radius[curr], abs(curr - num))
                min_heap.append((min_radius[curr], curr))
                
            if 0 <= left + 1 < len(houses):
                curr = houses[left + 1]
                min_radius[curr] = min(min_radius[curr], abs(curr - num))
                min_heap.append((min_radius[curr], curr)) 
                
        heapify(min_heap)
        
        
        while min_heap:
            cost, num = heappop(min_heap)
            idx = index_map[num]
            
            left = idx - 1
            right = idx + 1
            
            if left >= 0:
                new_cost = abs(num - houses[left]) + cost
                left_num = houses[left]
                if new_cost < min_radius[left_num]:
                    min_radius[left_num] = new_cost
                    heappush(min_heap, (min_radius[left_num], left_num))
            
            if right < len(houses):
                new_cost = abs(num - houses[right]) + cost
                right_num = houses[right]
                if new_cost < min_radius[right_num]:
                    min_radius[right_num] = new_cost
                    heappush(min_heap, (min_radius[right_num], right_num))
                    
        return max(list(min_radius.values()))