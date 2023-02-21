len1, len2  = tuple(map(int, input().split(" ")))
array1 = list(map(int, input().split(" ")))
array2 = list(map(int, input().split(" ")))
merged = []

ind1, ind2 = 0, 0
while ind1 < len1 or ind2 < len2:
    val1 = array1[ind1] if ind1 < len1 else array2[ind2] + 1
    val2 = array2[ind2] if ind2 < len2 else array1[ind1] + 1

    if val1 < val2:
        merged.append(val1)
        ind1 += 1
    else:
        merged.append(val2)
        ind2 += 1

print(*merged)
