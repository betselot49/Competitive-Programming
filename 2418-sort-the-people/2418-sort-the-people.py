class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
  #  < ======  using buble sort ======> 


#         for j in range(len(names)-1, 0, -1)
#            for i in range(j):
#                 if heights[i] < heights[i+1]:
#                     names[i], names[i+1] = names[i+1], names[i]
#                     heights[i], heights[i+1] = heights[i+1], heights[i]            
#         return names


#  < ==========   using Selection Sort  ========> 
    
        for i in range(len(names)):
            curMax = i
            for j in range(i, len(names)):
                if heights[j] > heights[curMax]:
                    curMax = j
                    
            heights[i], heights[curMax] =  heights[curMax], heights[i] 
            names[i], names[curMax] =  names[curMax], names[i]
            
        return names
            