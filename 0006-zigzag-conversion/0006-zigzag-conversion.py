class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        pointer, direction, zigzag = 0, "up", [""] * numRows
       
        for char in s:
            zigzag[pointer] += char
            if pointer == numRows - 1:
                direction = "down"
            elif pointer == 0:
                direction = "up"
                
            if direction == "up":
                pointer += 1
            elif direction == "down":
                pointer -= 1
            
        return "".join(zigzag)