N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split(" "))))

source = set()
sink = set()

for i in range(0, N-1):
    for j in range(i+1, N):
        if matrix[i][j] == 1:
            source.add(i+1)
            sink.add(j+1)
        if matrix[j][i] == 1:
            source.add(j+1)
            sink.add(i+1)

source_list = []
sink_list = []

for i in range(1, N+1):
    if i in source and i not in sink:
        source_list.append(i)
    elif i in sink and i not in source:
        sink_list.append(i)
    elif i not in sink and i not in source:
        source_list.append(i)
        sink_list.append(i)

source_list.sort()
sink_list.sort()
print(len(source_list), *source_list)
print(len(sink_list), *sink_list)
