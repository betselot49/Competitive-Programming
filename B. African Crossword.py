from collections import Counter, defaultdict


n, m = tuple(map(int, input().split(" ")))
grid = []
for _ in range(n):
    grid.append(input())

rowCounter = []
columnCounter = []

flag = True
for col in range(len(grid[0])):
    temp = defaultdict(int)
    for row in grid:
        if flag:
            rowCounter.append(Counter(row))
        temp[row[col]] += 1
    columnCounter.append(temp)
    flag = False


encoded = ""
for row in range(len(grid)):
    for col in range(len(grid[0])):
        char = grid[row][col]
        if rowCounter[row][char] == columnCounter[col][char] == 1:
            encoded += char

print(encoded)
