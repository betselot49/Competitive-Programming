class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.graph = defaultdict(list)
        for ind, node in enumerate(self.parent[1:]):
            self.graph[node].append(ind+1)
        self.locked = defaultdict(int)

    def lock(self, num: int, user: int) -> bool:
        if self.locked[num] == 0:
            self.locked[num] = user+1
            return True
        return False
    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] == user+1:
            self.locked[num] = 0
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        def locked_ancestor(node) -> bool:
            while node != -1:
                parent = self.parent[node]
                if self.locked[parent] != 0: return True
                node = parent
            return False
        
        def locked_descendant(node) -> bool:
            queue = deque([node])
            flag = False
            while queue:
                node = queue.popleft()
                if self.locked[node] != 0:
                    self.locked[node] = 0
                    flag = True
                for neighbour in self.graph[node]:
                    queue.append(neighbour)
            
            return flag
        
        if self.locked[num] != 0: return False
        if locked_ancestor(num): return False
        if locked_descendant(num):
            self.locked[num] = user+1
            return True
        return False
        
        
                


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)