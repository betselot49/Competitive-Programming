from collections import defaultdict, deque

while True:
    nums = int(input())
    if nums == 0:
        break
    N = int(input())
    flag = Truea
    graph = defaultdict(list)
    for _ in range(N):
        node1, node2 = list(map(int, input().split(" ")))

        graph[node1].append(node2)
        graph[node2].append(node1)

    color = {1:0}
    queue = deque([(1, 1)])
    while queue:
        node, turn = queue.popleft()

        for neighbour in graph[node]:
            if neighbour not in color:
                color[neighbour] = turn
                queue.append((neighbour, 1 - turn))
            elif color[neighbour] == color[node]:
                flag = False
                break
    if flag:
        print("BICOLOURABLE.")
    else:
        print("NOT BICOLOURABLE.")
