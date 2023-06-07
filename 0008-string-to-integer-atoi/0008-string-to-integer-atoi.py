class Solution(object):
    def myAtoi(self, s):
        # remember to do this question again by your self.
        MIN, MAX = -2 ** 31, 2 ** 31 - 1
        n, empty, sign = 0, True, 1
        for c in s:
            if empty:
                if c == ' ': continue 
                elif c == '-': sign = -1 
                elif c.isdigit(): n = int(c)  
                elif c != '+': return 0  
                empty = False 
            else:
                if c.isdigit():
                    n = n * 10 + int(c)
                    if sign * n > MAX: return MAX
                    elif sign * n < MIN: return MIN
                else: break   
        return sign * n 