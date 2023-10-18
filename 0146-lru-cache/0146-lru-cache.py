class LRUCache:

    def __init__(self, capacity: int):
        self.deque = deque([])
        self.key_value = {}
        self.curr_capacity = 0
        self.capacity = capacity
        self.update = defaultdict(int)
        
    def get(self, key: int) -> int:
        if key in self.key_value: 
            self.deque.append(key)
            self.update[key] += 1
            return self.key_value[key]
        return -1
            

    def put(self, key: int, value: int) -> None:
        if key in self.key_value:
            self.key_value[key] = value
            self.deque.append(key)
            self.update[key] += 1
        elif self.curr_capacity < self.capacity:
            self.deque.append(key)
            self.update[key] += 1
            self.key_value[key] = value
            self.curr_capacity += 1
        else:
            popped = self.deque.popleft()
            while self.update[popped] > 1:
                self.update[popped] -= 1
                popped = self.deque.popleft()
            del self.update[popped]
            del self.key_value[popped]
            
            self.deque.append(key)
            self.key_value[key] = value
            self.update[key] += 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)