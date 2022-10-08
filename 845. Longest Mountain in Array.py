class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        """
        
         [4,3,2,1,0,1,2,3,4,5,4,3,2,1,2,3,4,4,4,4,4,5,6,7,8]
         
                                    j
                                   /
                                  /
   _____i          /\            /
         \        /  \      ____/
          \      /    \    /
           \    /      \  /
            \  /        \/ 
             \/          
          
          peak = False   ---|
                            |---> initial position is niether peak nor valley
          valley = False ---|
          
          longestMount = 0
          
          
          [0,0,1,0,0,1,1,1,1,1]
             i     j
        """
        
        i, j, longestMount = 0, 1, 0
        while j < len(arr):
            peak, valley = False, False 
            if arr[j] != arr[j-1]:
                while j < len(arr) and arr[j] > arr[j-1]:
                    j += 1
                    peak = True
                while j < len(arr) and arr[j] < arr[j-1]:
                    j += 1
                    valley = True
            else:
                while j < len(arr) and arr[j] == arr[j-1]:
                    j += 1
            if (peak and valley) and (j - i >= 3):
                longestMount = max(longestMount, j - i)
            i = j - 1
        return longestMount
        
