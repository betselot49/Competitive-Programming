class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]
    
#         dec = defaultdict(list)
#         for edge in edges:
#             dec[edge[0]].append(edge[1])
#             dec[edge[1]].append(edge[0])
        
#         return edges[0][0] if len(dec[edges[0][0]]) > 2 else edges[0][1]

            