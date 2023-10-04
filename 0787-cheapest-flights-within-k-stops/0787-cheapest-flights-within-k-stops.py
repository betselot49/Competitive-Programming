class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        visited = set()
        
        for city1, city2, price in flights:
            graph[city1].append((city2, price))
     
        min_heap = [(0, src, 0)]
       
        while min_heap:
            price, city, level = heappop(min_heap)
            if (city, price) in visited: continue
                
            visited.add((city, price))
            
            if city == dst: return price
            
            if level > k: continue
                
            for curr_city, curr_price in graph[city]:

                heappush(min_heap, (price + curr_price, curr_city, level + 1))
       
        return -1