# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n = int(input())
roomNo = list(map(int, input().split(" ")))
ans = 0
seen = Counter(roomNo)
for room in roomNo:
    if seen[room] == 1:
        ans = room
print(ans)
