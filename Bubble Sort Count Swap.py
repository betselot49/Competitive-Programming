def countSwaps(a):
    swap_counter = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swap_counter += 1
    print(f"Array is sorted in {swap_counter} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[len(a) - 1]}")
    
