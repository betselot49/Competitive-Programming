def mergeSort(array, k):
    if len(array) < 2: return array

    low = 0
    high = len(array)
    mid = low + (high - low) // 2
    left = mergeSort(array[:mid], k)
    right = mergeSort(array[mid:], k)

    return merge(left, right, k)


def merge(left, right, k):
    left_idx = 0
    right_idx = 0
    winners = []
    winners_set = set()
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx][0] <= right[right_idx][0]:
            if right[right_idx][0] - left[left_idx][0] <= k:
                winners.append(left[left_idx])
            elif left[left_idx] in winners_set:
                winners.append(left[left_idx])
            winners_set.add(right[right_idx]) 
            left_idx += 1

        elif right[right_idx][0] < left[left_idx][0]:
            if left[left_idx][0] - right[right_idx][0] <= k:
                winners.append(right[right_idx])
            elif right[right_idx] in winners_set:
                winners.append(right[right_idx])
            winners_set.add(left[left_idx])
            right_idx += 1

    winners.extend(left[left_idx:]) 
    winners.extend(right[right_idx:])  

    return winners
    

n, k = list(map(int, input().split(" ")))
arr = list(map(int, input().split(" ")))

arr = [(num, idx) for idx, num in enumerate(arr)] 

winners = mergeSort(arr, k)
answer = [winner[1]+1 for winner in winners]
answer.sort()
print(*answer)
