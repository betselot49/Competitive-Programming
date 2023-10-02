class WordFilter:

    def __init__(self, words: List[str]):
        self.root = TreiNode()
        for idx, word in enumerate(words):
            for i in range(len(word)+1):
                curr_word = word[i:] + "{" + word
                self.insert(idx, curr_word)
                
    
    def f(self, pref: str, suff: str) -> int:
        find = suff + "{" + pref
        curr = self.root
        for char in find:
            index = ord(char) - 97
            if curr.children[index] == None: return -1
            curr = curr.children[index]
        return curr.index
    
    
    def insert(self, idx, word):
        curr = self.root
        for char in word:
            index = ord(char) - 97
            if curr.children[index] == None:
                curr.children[index] = TreiNode()
            curr.children[index].index = idx                    
            curr = curr.children[index]

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)


class TreiNode:
    def __init__(self):
        self.children = [None] * 27
        self.index = -1