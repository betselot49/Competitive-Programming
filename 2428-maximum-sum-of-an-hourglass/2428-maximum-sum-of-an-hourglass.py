class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        psum = []
        for row in grid:
            psumRow = [0]
            tempSum = 0
            for num in row:
                tempSum += num
                psumRow.append(tempSum)
            psum.append(psumRow)

        maxSum = 0
        curSum = 0
        for j in range(2, len(psum)):
            for i in range(3, len(psum[0])):
                curSum = psum[j][i] - psum[j][i-3] + psum[j-1][i-1] - psum[j-1][i-2] + psum[j-2][i] - psum[j-2][i-3]
                maxSum = max(maxSum, curSum)
        return maxSum