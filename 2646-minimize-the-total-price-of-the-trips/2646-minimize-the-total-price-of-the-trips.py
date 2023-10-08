class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        graph = defaultdict(list)
        freq = [0] * n
        
        for city1, city2 in edges:
            graph[city1].append(city2)
            graph[city2].append(city1)

        def bfs(start, end):
            min_heap = [(price[start], start)]
            parent = {start: None}
            seen = set()
            while min_heap:
                _price, city = heappop(min_heap)
                if city in seen: continue
               
                seen.add(city)
            
                if city == end: break 
                for child in graph[city]:
                    if child not in seen:
                        parent[child] = city
                        heappush(min_heap, (price[child] + _price, child))
            
            while end != None:
                freq[end] += 1
                end = parent[end]
                
        dp = {}
        def rec(node, half, parent):
            if (node, half, parent) in dp: return dp[(node, half, parent)]
            
            curr_price = price[node] * freq[node]
            curr_price *= 0.5 if half else 1
            for child in graph[node]:
                if child == parent: continue
        
                if half:
                    curr_price += rec(child, 0, node)
                else:
                    curr_price = min(curr_price + rec(child, 1, node), curr_price + rec(child, 0, node))
                
            dp[(node, half, parent)] = curr_price
            return dp[(node, half, parent)]
            
        for start, end in trips:
            bfs(start, end)
            
        return int(min(rec(0, 0, None), rec(0, 1, None)))