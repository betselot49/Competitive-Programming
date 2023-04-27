class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        def bfsRoom(room):
            queue = deque([room])
            while queue:
                curr_room = queue.popleft()
                visited[curr_room] = True
                for room in rooms[curr_room]:
                    if not visited[room]:
                        queue.append(room)
            return all(visited)
        return bfsRoom(0)