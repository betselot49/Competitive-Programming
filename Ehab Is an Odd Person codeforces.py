N = int(input())
 
array = list(map(int, input().split(" ")))
 
def checker(array):
    allEven = True
    allOdd = True
    
    for num in array:
        if num % 2 == 0:
            allEven = False
        else:
            allOdd = False
            
    if allEven or allOdd:
        return array
    
    array.sort()
    return array
 
print(*checker(array))
    
