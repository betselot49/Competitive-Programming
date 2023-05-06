class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = [True] * (right + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(right**0.5)+1):
            if not primes[i]: continue
            j = i ** 2
            while j < len(primes):
                primes[j] = False
                j += i
        if len(primes) < 4: return [-1, -1]
        
        # finding the first prime number
        idx1 = len(primes) - 1
        while idx1 >= left:
            if primes[idx1]:
                num2 = idx1
                break
            idx1 -= 1
            
        # explore usign left 
        answer = [-1, -1]
        min_diff = float('inf')
        idx = idx1 - 1
        while idx >= left:
            num1 = -1
            while idx >= left and not primes[idx]:
                idx -= 1
                
            if idx >= left:
                num1 = idx
                
            if num1 != -1 and (num2 - num1) <= min_diff:
                answer = [num1, num2]
                min_diff = num2 - num1
                
            num2 = num1
            idx -= 1
        
        return answer
            