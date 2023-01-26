class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(sqrt(c))
        
        while left <= right:
            sqaureSum = left ** 2 + right ** 2
            if sqaureSum == c:
                return True
            elif sqaureSum < c:
                left += 1
            else:
                right -= 1
        return False
            
            