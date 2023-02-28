class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        result = [1]
        manip = self.getRow(rowIndex-1)
        for i in range(1, len(manip)):
            result.append(manip[i] + manip[i-1])
        result.append(1)
        
        return result
    