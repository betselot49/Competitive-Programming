tests = int(input())
for _ in range(tests):
    length = int(input())
    array = list(map(int, input().split(" ")))

    curr = array[0]
    index = 0
    maxSum = 0

    while index < length:
        if curr > 0:
            while index < length and array[index] > 0:
                curr = max(curr, array[index])
                index += 1
        else:
            while index < length and array[index] < 0:
                curr = max(curr, array[index])
                index += 1

        maxSum += curr
        if index < length:
            curr = array[index]

    print(str(maxSum))
