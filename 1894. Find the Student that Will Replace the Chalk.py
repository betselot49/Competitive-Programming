class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        """
        Input: chalk = [3,4,1,2], k = 25
        
        Output: 1
        
        s = 0 => 3 chalk => k = 22
        s = 1 => 4 chalk => k = 18
        s = 2 => 1 chalk => k = 17
        s = 3 => 2 chalk => k = 15
        s = 0 => 3 chalk => k = 12
        s = 1 => 4 chalk => k = 8
        s = 2 => 1 chalk => k = 7
        s = 3 => 2 chalk => k = 5
        s = 0 => 3 chalk => k = 2
        s = 1 => 4 => replace!
        
        
        0:3, 1:4, 2:1, 3:2
        
        total = 20
        
        big O(2n)
        """
        
        chalk_used = 0
        for round in range(2):
            for replacer, c in enumerate(chalk):
                chalk_used += c
                if chalk_used > k:
                    return replacer
            chalk_used *= (k // chalk_used)
        
