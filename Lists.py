N = int(input())
ans = []

for i in range(N):
    command = input().split(" ")
    
    if (command[0] == "insert"):
        num1, num2 = int(command[1]), int(command[2])
        ans.insert(num1, num2)
    elif (command[0] == "print"):
        print(ans)
    elif (command[0] == "remove"):
        ans.remove(int(command[1]))
    elif (command[0] == "append"):
        ans.append(int(command[1]))
    elif (command[0] == "sort"):
        ans.sort()
    elif (command[0] == "pop"):
        ans.pop()
    elif (command[0] == "reverse"):
        ans.reverse()
            
