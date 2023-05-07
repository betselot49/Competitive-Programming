class Solution:
    def countArrangement(self, n: int) -> int:
        self.count = 0
        visited = set()
        path = []
        def backtrack(idx, n):
            if idx > n:
                self.count += 1
                return
            
            for i in range(1, n+1):
                if i not in visited and (i % idx == 0 or idx % i == 0):
                    path.append(i)
                    visited.add(i)
                    backtrack(idx+1, n)
                    path.pop()
                    visited.discard(i)
        
        backtrack(1, n)
        return self.count