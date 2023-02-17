len1, len2 = tuple(map(int, input().split(" ")))
array1 = list(map(int, input().split(" ")))
array2 = list(map(int, input().split(" ")))

count = []
index1 = 0
index2 = 0

curr = 0

for num in array2:
    while index1 < len(array1) and array1[index1] < num:
        curr += 1
        index1 += 1

    count.append(curr)

print(*count)



