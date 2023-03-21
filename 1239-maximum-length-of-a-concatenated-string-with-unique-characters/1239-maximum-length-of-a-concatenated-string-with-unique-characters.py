class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.alpha = {chr(i+97):0 for i in range(26)}
        self.length = 0
        self.max_length = 0
        
        def backtrack(path, idx):
            self.max_length = max(self.max_length, self.length)
            for i in range(idx, len(arr)):
                if len(arr[i]) != len(set(arr[i])):
                    continue
                    
                seen = False
                for ch in arr[i]:
                    if self.alpha[ch] > 0:
                        seen = True
                        break
                
                if seen:
                    continue
            
                for ch in arr[i]:
                    self.alpha[ch] = 1
                
                self.length += len(arr[i])
                backtrack(path[:], i+1)
                for ch in arr[i]:
                    self.alpha[ch] = 0
                    
                self.length -= len(arr[i])
        
        backtrack([], 0)
        return self.max_length