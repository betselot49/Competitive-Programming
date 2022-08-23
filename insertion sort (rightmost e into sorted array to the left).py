def insertionSort1(n, arr):
    unsorted_num = arr[len(arr) - 1]
    for i in range((len(arr) - 2), -1, -1):
        if unsorted_num < arr[i]:
            arr[i + 1] = arr[i]
            for item in arr:
                print(item, end=" ")
            print()
        else:
            arr[i + 1] = unsorted_num
            for item in arr:
                print(item, end=" ")
            print()
            break
    if arr[0] > unsorted_num:
        arr[0] = unsorted_num
        for item in arr:
            print(item, end=" ")
        print()
       
# or

def insertionSort1(n, arr):
    unsorted_num = arr[len(arr) - 1]
    i = len(arr) - 2
    while i > -1:
        if unsorted_num < arr[i]:
            arr[i + 1] = arr[i]
            i -= 1
        else:
            arr[i + 1] = unsorted_num
            i = -1
        for item in arr:
            print(item, end=" ")
        print()
    if arr[0] > unsorted_num:
        arr[0] = unsorted_num
        for item in arr:
            print(item, end=" ")
        print()
