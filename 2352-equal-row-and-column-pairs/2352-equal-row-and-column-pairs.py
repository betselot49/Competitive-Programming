class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:        
        rowDict = defaultdict(int)
        
#         for row in grid:  # add rows with their frequency in rowDict in their string form
#             key = ""
#             for column in row:
#                 key += str(column) + "#"
#             rowDict[key] += 1
            
#         count = 0
#         for column in range(len(grid[0])):  # count each column's match in rowDict 
#             key = ""
#             for row in grid:
#                 key += str(row[column]) + "#"  # to scape cases like [[11,1],[1,11]]
#             count += rowDict[key]    
        
#         return count

#  << =========== OR using tuples instead of string with # init =========== >>

        for row in grid:
            rowDict[tuple(row)] += 1
    
        count = 0
        for column in range(len(grid[0])):
            key = []
            for row in grid:
                key.append(row[column])

            count += rowDict[tuple(key)]
            
        return count