class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)] 
        nearest_zero = [[float('inf')] * len(mat[0]) for _ in range(len(mat))]
        queue = deque([])
        
        # check the validity of current cell
        def isValid(row, col):
            row_inbound = 0 <= row < len(mat)
            col_inbound = 0 <= col < len(mat[0])
            return row_inbound and col_inbound
                
        # find the all zeros in the matrix and append it to queue
        def findZero():
            for row in range(len(mat)):
                for col in range(len(mat[0])):
                    if mat[row][col]: continue
                    queue.append((row, col, 0))
            return queue
                        
        iteration = 0
        queue = findZero()
        while queue:
            row, col, cost = queue.popleft()
            # keep explore if only you find zero with less cost or shorter path
            iteration += 1
            if nearest_zero[row][col] <= cost: continue
            nearest_zero[row][col] = cost 
            
            for cord1, cord2 in DIRECTIONS:
                n_row, n_col = row + cord1, col + cord2
                if not isValid(n_row, n_col): continue
                queue.append((n_row, n_col, cost + 1)) if mat[n_row][n_col] == 1 else queue.append((n_row, n_col, 0))
                
        return nearest_zero
        