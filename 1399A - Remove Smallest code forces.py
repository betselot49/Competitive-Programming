test = int(input())

for _ in range(test):
    size = int(input())
    arr = list(map(int, input().split(" ")))
    arr.sort()
    
    flag = True
    for num in range(size-1):
        if abs(arr[num] - arr[num+1]) > 1:
            flag = False
            break
        
    if flag:
        print("YES")
    else:
        print("NO")
