class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        sc = 0
        sr = 0
        ec = len(matrix[0])
        er = len(matrix)
        i = sc
        j = sr
        ans = []
        counter = 0
        while counter < len(matrix[0] * len(matrix)):
            for i in range(sc, ec):
                if counter < len(matrix[0] * len(matrix)):
                    ans.append(matrix[j][i])
                    counter += 1
            sr += 1

            for j in range(sr, er):
                if counter < len(matrix[0] * len(matrix)):
                    ans.append(matrix[j][i])
                    counter += 1
            ec -= 1

            for i in range(ec - 1, sc - 1, -1):
                if counter < len(matrix[0] * len(matrix)):
                    ans.append(matrix[j][i])
                    counter += 1
            er -= 1

            for j in range(er - 1, sr - 1, -1):
                if counter < len(matrix[0] * len(matrix)):
                    ans.append(matrix[j][i])
                    counter += 1
            sc += 1
        
        return ans