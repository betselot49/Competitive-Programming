def superSetChecker():
    superSet = set(map(int, input().split(" ")))
    lenSupSet = len(superSet)

    numSet = int(input())
    for i in range(numSet):
        subSet = set(map(int, input().split(" ")))
        
        if len(superSet) <= len(subSet):
            return False
        
        for num in subSet:
            if num not in superSet:
                return False
            
    return True

print(superSetChecker())
