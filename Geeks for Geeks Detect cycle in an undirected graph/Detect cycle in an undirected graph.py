from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		def dfs(node, parent):
		    if node != parent and node in path: return True
		    path.add(node)
		    visited.add(node)
		    for neighbour in adj[node]:
		        if parent == neighbour: continue
		        if dfs(neighbour, node): return True
		    
		    path.remove(node)
		    return False
		
		visited = set()    
		for i in range(V):
		    if i in visited: continue
		    path = set()
		    if dfs(i, None): return True
		 
		return False  
