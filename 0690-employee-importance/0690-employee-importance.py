"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(list)
        for employee in employees:
            graph[employee.id] = [employee.importance, employee.subordinates]
        
        self.importance = 0
        def dfs(id):
            self.importance += graph[id][0]
            for sub_id in graph[id][1]:
                dfs(sub_id)
        dfs(id)
        return self.importance
            