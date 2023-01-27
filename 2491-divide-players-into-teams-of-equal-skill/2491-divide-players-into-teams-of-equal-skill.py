class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        curSum = skill[0] + skill[-1]
        curProd = skill[0] * skill[-1] 
        left = 1
        right = len(skill) - 2
        
        while left < right:
            if skill[left] + skill[right] != curSum:
                return -1
            
            curProd += skill[left] * skill[right]
            left += 1
            right -= 1
            
        return curProd