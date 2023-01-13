class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        unsorted = 0
        
        for col in range(len(strs[0])):
            Sorted = True
            for row in range(len(strs) - 1):
                if strs[row][col] > strs[row + 1][col]:
                    Sorted = False
                    break
                
            if not Sorted:
                unsorted += 1
                
        return unsorted
        