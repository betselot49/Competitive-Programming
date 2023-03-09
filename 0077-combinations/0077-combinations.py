class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
         
        def combination(start, comb):
            if len(comb) == k:
                result.append(comb.copy())
                return 
            
            for i in range(start, n+1):
                comb.append(i)
                combination(i+1, comb)
                comb.pop()
                
        combination(1, [])
        return result
        