# Enter your code here. Read input from STDIN. Print output to STDOUT
tests = int(input())
ans = []


for i in range(tests):
    cubes = int(input())
    length = input().split(" ")
    
    i = 0
    j = cubes - 1
    
    stack = []
    if int(length[i]) >= int(length[j]):
        stack.append(int(length[i]))
        i += 1
    else:
        stack.append(int(length[j]))
        j -= 1
    while i <= j:
        if stack[-1] >= int(length[i]) and stack[-1] >= int(length[j]):
            if int(length[i]) >= int(length[j]):
                stack.append(int(length[i]))
                i += 1
            else:
                stack.append(int(length[j]))
                j -= 1
        else:
            ans.append("No")  
            break  
    if i > j:
        ans.append("Yes")
    
for a in ans:
    print(a)
    
