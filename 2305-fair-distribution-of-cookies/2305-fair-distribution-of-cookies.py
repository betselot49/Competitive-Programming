class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        children = [0]*k
        
        def distribute(idx):
            if idx == len(cookies):
                return max(children) 
            
            ans = float('inf')
            for i in range(min(k, idx+1)):
                children[i] += cookies[idx]
                ans = min(ans, distribute(idx+1))
                children[i] -= cookies[idx]
            return ans
        
        return distribute(0)
    