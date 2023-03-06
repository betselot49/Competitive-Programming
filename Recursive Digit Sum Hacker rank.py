def Super(n):
    if int(n) // 10 == 0:
        return int(n)
    
    new = 0
    for num in n:
        new += int(num)
    
    return Super(str(new))

def superDigit(n, k):
    new = 0
    for num in n:
        new += int(num)
    
    return Super(str(new)*k)
