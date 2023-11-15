class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        i = 0
        while i < len(asteroids):
            if not stack or asteroids[i] > 0 or stack[-1] < 0:
                stack.append(asteroids[i])
                i += 1
            elif stack[-1] == abs(asteroids[i]):
                stack.pop()
                i += 1
            elif stack[-1] > abs(asteroids[i]):
                i += 1
            elif stack[-1] < abs(asteroids[i]):
                stack.pop()
                
        return stack
         
                    