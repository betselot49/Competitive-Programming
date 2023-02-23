length, k = tuple(map(int,input().split(' ')))
array = list(map(int,input().split(' ')))
array.sort()
 
if k == 0:
    if array[k] == 1:
        print(-1)
    else:
        print(array[k]-1)
 
 
elif k < length and array[k-1] == array[k]:
    print(-1)
else:
    print(array[k-1])
