class Solution:
    def removeDuplicates(self, word: str, k: int) -> str:
        stack = [["", 0]]
        for char in word:
            if stack[-1][0] == char:
                stack[-1][1] += 1
            else:
                stack.append([char, 1])
            
            if stack[-1][1] == k:
                stack.pop()
        ans = ""        
        for char, count in stack:
            ans += char * count
        
        return ans