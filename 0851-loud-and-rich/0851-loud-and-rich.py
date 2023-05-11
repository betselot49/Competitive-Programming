class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * len(quiet)
        for node1, node2 in richer:
            graph[node1].append(node2)
            indegree[node2] += 1
        
        # initially number itself could be answer
        answer = [i for i in range(len(quiet))]
        
        queue = deque([i for i in range(len(indegree)) if not indegree[i]])
        quiet_value = { quietness: ind for ind, quietness in enumerate(quiet) }
        while queue:
            node = queue.popleft()
            for neighbour in graph[node]:
                # update answer[neighbour] with minimun quiet_value of current value and the node's quiet value
                answer[neighbour] = quiet_value[min(quiet[answer[neighbour]], quiet[answer[node]])]
                indegree[neighbour] -= 1
                if not indegree[neighbour]:
                    queue.append(neighbour)
        return answer
        
        