from collections import Counter

testCase = int(input())
for i in range(testCase):
    info = list(map(int, input().split(" ")))
    orbits = Counter(list(map(int, input().split(" "))))
    cost = info[1]
    
    minCost = 0
    
    for planets in orbits.values():
        if cost <= planets:
            minCost += cost
        else:
            minCost += planets
    
    print(minCost)
