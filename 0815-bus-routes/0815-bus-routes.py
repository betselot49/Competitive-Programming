class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0
        routes = list(map(set, routes))
        graph = collections.defaultdict(set)
        for i, r1 in enumerate(routes):
            for j in range(i+1, len(routes)):
                r2 = routes[j]
                if any(r in r2 for r in r1):
                    graph[i].add(j)
                    graph[j].add(i)

        seen, targets = set(), set()
        for node, route in enumerate(routes):
            if source in route: seen.add(node)
            if target in route: targets.add(node)

        queue = [(node, 1) for node in seen]
        for node, depth in queue:
            if node in targets: return depth
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth+1))
        return -1