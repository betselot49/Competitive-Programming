from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def AddEdge(self, node1, node2):
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def Vertex(self, node):
        return self.graph[node]        


vertices = int(input())
test = int(input())
graph = Graph()
operations = []
for _ in range(test):
    operations.append(list(map(int, input().split(" "))))

for operation in operations:
    if operation[0] == 1:
        graph.AddEdge(operation[1], operation[2])
    else:
        vertex = graph.Vertex(operation[1])
        print(*vertex)
