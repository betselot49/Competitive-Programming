class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.valid = []
        def backtrack(path, idx):
            if len(path) == 4 and idx == len(s):
                self.valid.append(".".join(path))
                return 
            if len(path) == 4: return 
                
            for i in range(idx, len(s)):
                curr = s[idx:i+1]
                if len(curr) == len(str(int(curr))) and 0 <= int(curr) <= 255:
                    path.append(curr)
                    backtrack(path[:], i+1)
                    path.pop()
                
        backtrack([], 0)
        return self.valid