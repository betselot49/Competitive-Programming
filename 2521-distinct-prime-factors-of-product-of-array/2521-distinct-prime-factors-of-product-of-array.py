class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        self.set = set()
        def primeFactor(num):
            for i in range(2, int(num ** 0.5) + 1):
                while num > 1 and num % i == 0:
                    num /= i
                    self.set.add(i)
            if num > 1:
                self.set.add(num)
                    
        for num in nums:
            primeFactor(num)
        return len(self.set)
            
        
                    
        