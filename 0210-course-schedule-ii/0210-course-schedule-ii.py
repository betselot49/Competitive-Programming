class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indgree = defaultdict(int)
        
        for course in prerequisites:
            indgree[course[0]] += 1
            
        
        for course in prerequisites:
            graph[course[1]].append(course[0])
            
        queue = deque([])
        for course in range(numCourses):
            if indgree[course] == 0:
                queue.append(course)
                
        order = []
        while queue:
            curr = queue.popleft()
            order.append(curr)
            for next_course in graph[curr]:
                indgree[next_course] -= 1
                if  indgree[next_course]  == 0:
                    queue.append(next_course)
                    
        if len(order) != numCourses: return []
        return order