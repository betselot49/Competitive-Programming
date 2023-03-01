class Solution:
    def recReverse(self, word, left, right):
        if right - left > 1:
            self.recReverse(word, left + 1, right - 1)
        word[left], word[right] = word[right], word[left]
        
    def reverseString(self, s: List[str]) -> None:
        self.recReverse(s, 0, len(s)-1)