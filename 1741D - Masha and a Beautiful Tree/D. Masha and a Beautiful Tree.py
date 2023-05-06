def mergeSort(array):
    if len(array) < 2:
        return array
    low = 0
    high = len(array)
    mid = low + (high - low) // 2

    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])
    return merge(left, right)


def merge(left, right):
    global possible
    global swap
  
    if possible and left and right:
        if left[0] - right[-1] == 1:
            right.extend(left)
            swap += 1
            return right
        elif right[0] - left[-1] == 1:
            left.extend(right)
            return left
    possible = False
    swap = -1

test = int(input())

for _ in range(test):
    possible = True
    swap = 0
    length = int(input())
    arr = list(map(int, input().split()))

    mergeSort(arr)
    print(swap)
