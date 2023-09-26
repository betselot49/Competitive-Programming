class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            idx = ord(char) - 97
            if curr.children[idx] == None:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
            
        curr.is_End = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            idx = ord(char) - 97
            if curr.children[idx] == None:
                return False
            curr = curr.children[idx]
        
        return curr.is_End
            
            
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            idx = ord(char) - 97
            if curr.children[idx] == None:
                return False
            curr = curr.children[idx]
        
        return True
        


class TrieNode:
    def __init__(self):
        self.is_End = False
        self.children = [ None for _ in range(26) ]
        
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)