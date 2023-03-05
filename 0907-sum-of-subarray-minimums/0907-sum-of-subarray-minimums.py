class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:      
        inc_stack = []
        total = 0
        min_sum = 0
        
        for num in arr:  
            count = 0
            
            # maintain the stack in increasing order
            while inc_stack and inc_stack[-1][0] > num:
                pop = inc_stack.pop()
                total -= (pop[0] * pop[1])
                count += pop[1]
                
            count += 1
            if inc_stack and inc_stack[-1][0] == num:
                inc_stack[-1][1] += count
                total += (num * count)
            else:
                inc_stack.append([num, count])
                total += (num * count)
        
            min_sum += total
            
        return min_sum % (10 ** 9 + 7)
            
                
        
                
                