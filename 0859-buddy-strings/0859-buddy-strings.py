class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal) or len(s) == 1: return False
        if s == goal and len(set(s)) < len(s): return True
        
        left = 0
        right = len(s) - 1
        
        s = [i for i in s]
        goal = [g for g in goal]
        
        i = 0
        while i < len(s):
            if s[i] != goal[i]:
                left = i
                break
            i += 1
            
        j = right
        while j >= 0:
            if s[j] != goal[j]:
                right = j
                break
            j -= 1
            
        s[left], s[right] = s[right], s[left]
        return "".join(s) == "".join(goal)