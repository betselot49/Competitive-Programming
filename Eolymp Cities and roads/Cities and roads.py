N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

counter = 0
for row in range(N-1):
    for col in range(row+1, N):
        counter += matrix[row][col]
print(counter)
