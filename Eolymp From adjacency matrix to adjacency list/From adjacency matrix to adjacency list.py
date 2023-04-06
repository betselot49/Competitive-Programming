from collections import defaultdict

N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

graph = defaultdict(list)
for row_idx, row in enumerate(matrix):
    for col_idx, bit in enumerate(row):
        if bit == 1:
            graph[row_idx+1].append(col_idx+1)

for i in range(1, N+1):
    print(len(graph[i]), *graph[i])

