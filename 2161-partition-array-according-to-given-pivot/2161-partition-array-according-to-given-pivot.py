class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lessThanPivot, equalToPivot, greaterThanPivot = [], [], []
       
        for num in nums:
            if num < pivot:
                lessThanPivot.append(num)
            elif num > pivot:
                greaterThanPivot.append(num)
            else:
                equalToPivot.append(num)
                
        
        lessThanPivot.extend(equalToPivot)
        lessThanPivot.extend(greaterThanPivot)
        
        return lessThanPivot
    
        