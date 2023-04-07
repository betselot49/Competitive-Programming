class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = set()
        outdegree = set()
        for node1, node2 in edges:
            outdegree.add(node1)
            indegree.add(node2)
        small_set = []
        for i in range(n):
            if i in outdegree and i not in indegree:
                small_set.append(i)
        return small_set