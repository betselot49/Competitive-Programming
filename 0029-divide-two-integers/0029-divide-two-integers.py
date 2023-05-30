class Solution:    
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==-2147483648 and divisor==-1:
            return 2147483647        
        a=abs(dividend)
        b=abs(divisor)        
        ans=0
        for i in range(31,-1,-1):            
            if b << i <= a:
                a-= b << i                
                ans+=1 << i
        if dividend<0 and divisor<0:            
            return ans
        if dividend <0 or divisor<0:            
            return -ans
        return ans
    