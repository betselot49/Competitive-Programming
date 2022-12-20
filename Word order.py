from collections import defaultdict

n = int(input())
words = []
for i in range(n):
    x = input()
    words.append(x)
    
hashM = defaultdict(lambda: 0)
for word in words:
    hashM[word] += 1
    
print(len(hashM))
ans = ""
for word in hashM:
    print(hashM[word], end=" ")
