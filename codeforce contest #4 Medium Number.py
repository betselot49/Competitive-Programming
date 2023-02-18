n = int(input())
 
for _ in range(n):
    test_case = list(map(int, input().split(" ")))
    test_case.sort()
    print(str(test_case[1]))
