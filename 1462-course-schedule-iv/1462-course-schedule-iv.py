class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        incoming = defaultdict(int)
        ans = [set() for _ in range(numCourses)]
        for u, v in prerequisites:
            graph[u].append(v)
            incoming[v] += 1
        
        queue = deque()
        for i in range(numCourses):
            if incoming[i] == 0:
                queue.append(i)
        
        while queue:
            course = queue.popleft()
            for neighbours in graph[course]:
                incoming[neighbours]  -= 1
                ans[neighbours].update(ans[course])
                ans[neighbours].add(course)
                if incoming[neighbours] == 0:
                    queue.append(neighbours)
        result = []
        for i in range(len(queries)):
            u, v = queries[i]
            if u in ans[v]:
                result.append(True)
            else:
                result.append(False)
        return result