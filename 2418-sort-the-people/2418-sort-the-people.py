class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        j = len(heights) - 1
        while j > 0:
            i = 0
            while i < j:
                if heights[i] < heights[i+1]:
                    names[i], names[i+1] = names[i+1], names[i]
                    heights[i], heights[i+1] = heights[i+1], heights[i]
                i += 1
            j -= 1
            
        return names
            