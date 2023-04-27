class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def bfsRoom(room, rooms, visited):
            queue = deque([room])
            while queue:
                curr_room = queue.popleft()
                visited[curr_room] = True
                for room in rooms[curr_room]:
                    if not visited[room]:
                        queue.append(room)
            return all(visited)
        visited = [False] * len(rooms)
        return bfsRoom(0, rooms, visited)