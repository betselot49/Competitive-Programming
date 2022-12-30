from collections import defaultdict

tests = int(input())

for i in range(tests):
    length = int(input())
    elements = list(map(int, input().split(" ")))
    string = input()
    
    defDict = defaultdict(str)
    flag = True
    for index, num in enumerate(elements):
        if defDict[num] and defDict[num] != string[index]:
            flag = False
            break
        defDict[num] = string[index]
    if flag:
        print("YES")
    else:
        print("NO")
