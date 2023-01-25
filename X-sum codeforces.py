from collections import defaultdict

test = int(input())
for _ in range(test):
    rowSize, colSize = tuple(map(int, input().split(" ")))
    
    diag1 = defaultdict(int)
    diag2 = defaultdict(int)
    
    matrix = []
    for _ in range(rowSize):
        grid = list(map(int, input().split(" ")))
        matrix.append(grid)
    
    for row in range(rowSize):
        for col in range(colSize):
            diag1[row-col] += matrix[row][col]
            diag2[row+col] += matrix[row][col]
            
    maxSum = 0
    for row in range(rowSize):
        for col in range(colSize):
            curSum = diag1[row-col] + diag2[row+col] - matrix[row][col]
            maxSum = max(maxSum, curSum)
            
    print(str(maxSum))
