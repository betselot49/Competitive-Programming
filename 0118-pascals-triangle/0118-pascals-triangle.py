class Solution:
    def __init__(self):
        self.pascal_array = []
        
    def pascal(self, num):
            if num == 1:
                self.pascal_array.append([1])
                return [1]
            
            inner = self.pascal(num - 1)
            generated = [1]
            for i in range(1, len(inner)):
                generated.append(inner[i]+inner[i-1])
            generated.append(1)
            
            self.pascal_array.append(generated)
            return generated
    
    def generate(self, numRows: int) -> List[List[int]]:
        self.pascal(numRows)
        return self.pascal_array
        
        