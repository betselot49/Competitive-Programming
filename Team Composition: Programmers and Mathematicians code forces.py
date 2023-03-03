test = int(input())
for _ in range(test):
    a, b = map(int, input().split())
    
    max_team = (a + b) // 4
    print(min(max_team, min(a, b)))
    
