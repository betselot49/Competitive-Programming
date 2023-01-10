class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1, num2 = num1.split("+"), num2.split("+")
        real1, real2 = int(num1[0]), int(num2[0])
        imag1, imag2 = int(num1[1][:-1]), int(num2[1][:-1])
      
        realProduct = (real1 * real2) - (imag1 * imag2) # we substruct since (i*i) = -1
        imagProduct = (real1 * imag2) + (imag1 * real2)
        
        return str(realProduct) + "+" + str(imagProduct) + "i"
          