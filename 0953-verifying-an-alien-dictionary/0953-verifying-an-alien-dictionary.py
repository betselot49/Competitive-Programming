class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        from collections import defaultdict
        hashMap = defaultdict(lambda: 0)
        for i, char in enumerate(order):
            hashMap[char] = i
        
        i = 1
        while i < len(words):
            j = 0
            while j < len(words[i-1]):
                if len(words[i]) == j:
                    return False
                elif hashMap[words[i-1][j]] == hashMap[words[i][j]]:
                    j += 1
                elif hashMap[words[i-1][j]] > hashMap[words[i][j]]:
                    return False
                else:
                    break
            i += 1
        return True