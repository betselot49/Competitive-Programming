class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(set)
        indegree = [0] * numCourses
        for course1, course2 in prerequisites:
            graph[course2].add(course1)
            indegree[course1] += 1
            
        prerequisite_set = [set() for _ in range(numCourses)]
        queue = deque([])
        
        for node in range(numCourses):
            if indegree[node] == 0:
                queue.append(node)
                
        while queue:
            node = queue.popleft()
            for neighbour in graph[node]:
                prerequisite_set[neighbour].update(prerequisite_set[node])
                prerequisite_set[neighbour].add(node)
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
                    
        thruth_val = []
        for c1, c2 in queries:
            if c2 in prerequisite_set[c1]:
                thruth_val.append(True)
            else:
                thruth_val.append(False)
                
        return thruth_val