class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(lambda : set())
        indegree = defaultdict(int)
        for course1, course2 in prerequisites:
            graph[course2].add(course1)
            indegree[course1] += 1
            
        prereq_set = [set() for _ in range(numCourses)]
        queue = deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                
        while queue:
            curr = queue.popleft()
            for neighbour in graph[curr]:
                prereq_set[neighbour].update(prereq_set[curr])
                prereq_set[neighbour].add(curr)
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        
        answer = []
        for course1, course2 in queries:
            if course2 in prereq_set[course1]:
                answer.append(True)
            else:
                answer.append(False)
                
        return answer
                
        
            
       