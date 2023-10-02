class Solution:
    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()    
            else:
                curr.children[char].count += 1
            curr = curr.children[char]
            
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        self.root = TrieNode()
        score = []
        
        for word in words:
            self.insert(word)
    
        for word in words:
            curr, total = self.root, 0
            for char in word:
                if char in curr.children:
                    total += curr.children[char].count
                    curr = curr.children[char]
                else:
                    break
               
            score.append(total)
    
        return score
    
    
class TrieNode:
    def __init__(self):
        self.count = 1
        self.children = {}
 
