from collections import defaultdict

length = list(map(int, input().split(" ")))

dict1 = defaultdict(list)

for i in range(length[0]):
    dict1[input()].append(str(i+1))

for i in range(length[1]):
    char = input()
    if dict1[char]:
        print(" ".join(dict1[char]))
    else:
        print("-1")
