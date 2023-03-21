class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        self.building = [0] * n
        self.max = 0
        
        def backtrack(path, idx):
            if not any(self.building):
                self.max = max(self.max, len(path))
            
            for i in range(idx, len(requests)):
                req = requests[i]
                self.building[req[0]] -= 1
                self.building[req[1]] += 1
                path.append(req)
                backtrack(path[:], i+1)
                path.pop()
                self.building[req[0]] += 1
                self.building[req[1]] -= 1
        
        backtrack([], 0)
        return self.max