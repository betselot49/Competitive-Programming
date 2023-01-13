class Solution:
    def binarySearchMatrix(self, matrix, target):
        if len(matrix) == 1:
            return matrix[0]
        
        mid = len(matrix) // 2
        left, right = matrix[:mid], matrix[mid:] 
        if left[-1][-1] >= target:
            return self.binarySearchMatrix(left, target)
        else:
            return self.binarySearchMatrix(right, target)
        
        
    def binarySearch(self, array, target):
        if len(array) == 1:
            return array[0]
        
        mid = len(array) // 2
        left, right = array[:mid], array[mid:]
        if left[-1] >= target:
            return self.binarySearch(left, target)
        else:
            return self.binarySearch(right, target)
        
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        targetArray = self.binarySearchMatrix(matrix, target)
        targetNumber = self.binarySearch(targetArray, target)
        return targetNumber == target
        
        