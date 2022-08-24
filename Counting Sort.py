def countingSort(arr):
    result = [0] * 100
    for num in arr:
        result[num] += 1
    return result
        
