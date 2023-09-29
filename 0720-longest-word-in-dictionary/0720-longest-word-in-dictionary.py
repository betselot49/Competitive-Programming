class Solution:
    def longestWord(self, words: List[str]) -> str:
        self.root = TrieNode()
        for word in words:
            curr = self.root
            for char in word:
                curr = curr.children[char]
                
            curr.is_End = True
            
        longest_word = ""
        for word in words:
            if self.validate(word):
                longest_word = self.max_string(longest_word, word)
                
        return longest_word

        
    def validate(self, word):
        curr = self.root
        for char in word:
            if not curr.children[char].is_End: return False
            curr = curr.children[char]
            
        return True
    
    def max_string(self, word1, word2):
        if len(word1) == len(word2):
            return min(word1, word2)
        
        if len(word1) > len(word2): return word1
        return word2
                    
class TrieNode:
    def __init__(self):
        self.children = defaultdict(lambda : TrieNode())
        self.is_End = False