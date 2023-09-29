class MapSum:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        curr = self.root
        val += self.search(key)

        for char in key:
            curr.children[char].value += val
            curr = curr.children[char]
        curr.is_End = True

    def sum(self, prefix: str) -> int:
        curr = self.root
        for char in prefix:
            curr = curr.children[char]
        
        return curr.value
    
    def search(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children: return 0
            curr = curr.children[char]
        
        if not curr.is_End: return 0
        
        child_value = 0 
        for node in curr.children.values():
            child_value += node.value
            
        return child_value - curr.value
        


class TrieNode:
    def __init__(self):
        self.children = defaultdict(lambda : TrieNode())
        self.value = 0
        self.is_End = False

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)