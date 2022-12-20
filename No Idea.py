# Enter your code here. Read input from STDIN. Print output to STDOUT
nm = input().split(" ")
n = input().split(" ")
a = input().split(" ")
b = input().split(" ")

setA = set() 
setB = set()
ans = 0

for num in a:
    setA.add(int(num))
for num in b:
    setB.add(int(num))
    
for num in n:
    if int(num) in setA:
        ans += 1
    elif int(num) in setB:
        ans -= 1
        
print(ans)
