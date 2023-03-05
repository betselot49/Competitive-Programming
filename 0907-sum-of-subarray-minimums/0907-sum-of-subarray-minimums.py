class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:      
        inc_stack = []
        total = min_sum = 0
        MOD = 10 ** 9 + 7 
        
        for num in arr:  
            count = 1
            while inc_stack and inc_stack[-1][0] >= num:
                pop = inc_stack.pop()
                total -= (pop[0] * pop[1])
                count += pop[1]
            
            inc_stack.append([num, count])
            total += (num * count)
            min_sum += total
            
        return min_sum % MOD
            
                
        
                
                