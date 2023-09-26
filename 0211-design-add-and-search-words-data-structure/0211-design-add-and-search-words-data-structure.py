class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            idx = ord(char) - 97
            if curr.children[idx] == None:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
            
        curr.is_End = True
        

    def search(self, word: str) -> bool:
        def searchRec(Trie, idx):
            if idx == len(word):
                return Trie.is_End
            
            exist = False
            curr = ord(word[idx]) - 97
            if word[idx] != "." and Trie.children[curr] != None:
                exist = searchRec(Trie.children[curr], idx + 1)
                
            elif word[idx] == ".":
                for i in range(26):
                    if Trie.children[i] != None:
                        exist = exist or searchRec(Trie.children[i], idx + 1)
            
            return exist
        
        return searchRec(self.root, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

class TrieNode():
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_End = False
        