class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:   
        ans = []
        for j in range(len(matrix[0])):
            temp = []
            i = 0
            while i < len(matrix):
                temp.append(matrix[i][j])
                i += 1
            ans.append(temp)
        return ans
                