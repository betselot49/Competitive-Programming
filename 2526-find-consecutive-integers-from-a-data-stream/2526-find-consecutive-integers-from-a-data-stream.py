class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.stream = []
        self.invalid = -1  # holds the index of number not equal to value

    def consec(self, num: int) -> bool:
        self.stream.append(num)
        
        if num != self.value:
            self.invalid = len(self.stream) - 1
            return False
    
        if len(self.stream) - (self.invalid + 1) >= self.k:  # checks the last k numbers in num
            return True
        return False
         
            
            


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
