numInput = int(input())
for i in range(numInput):
    sizes = input().split(" ")
    
    sizeNotation = {"L": 2, "M": 1, "S": 0}
    
    left = sizes[0]
    right = sizes[1]
    
    if sizeNotation[left[-1]] > sizeNotation[right[-1]]:
        print(">")
    elif sizeNotation[left[-1]] < sizeNotation[right[-1]]:
        print("<")
    elif sizeNotation[left[-1]] == sizeNotation[right[-1]]:
        if len(left) < len(right):
            if left[-1] == "S":
                print(">")
            else:
                print("<")
        elif len(left) > len(right):
            if left[-1] == "S":
                print("<")
            else:
                print(">")
        else:
            print("=")
