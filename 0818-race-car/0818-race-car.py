class Solution:
    def racecar(self, target: int) -> int:
        position, speed, sequence = 0, 1, 0
        queue = deque([(position, speed, sequence)])
        visited = set([(0, 1)])
        
        while queue:
            position, speed, sequence = queue.popleft()
            if position == target: return sequence
        
            if (position + speed, speed * 2) not in visited:
                queue.append((position + speed, speed * 2, sequence + 1))
                visited.add((position + speed, speed * 2))
            
            speed = -1 if speed > 0 else 1
            if (position, speed) not in visited:
                queue.append((position, speed, sequence + 1))
                visited.add((position, speed))
        
        return -1
        